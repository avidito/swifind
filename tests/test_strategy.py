import pytest
import types

from swifind.strategy import Strategy, Plan
from swifind.exception import (LogicalError,
                               ObjectTypeError)

class TestStrategyInitiation(object):
    def test_object_type(self):
        strategy_test = Strategy()
        assert isinstance(strategy_test, Strategy)
        assert strategy_test.head is None
        assert strategy_test.tail is None
        assert strategy_test.rank == 0

class TestStrategyPlanLogicCheck(object):
    def test_with_valid_plan(self):
        strategy_test = Strategy()
        strategy_test.plan_logic_check('ORIGIN', 1)

        strategy_test.add_activity('ORIGIN', lambda x: x, 1)
        strategy_test.plan_logic_check('PICK', 2)

    def test_with_invalid_plan(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x, 1)

        msg = "Error at line 2: 'ORIGIN' activity must be the first component and cannot be redefined."
        with pytest.raises(LogicalError, match=f"^{msg}$") as exception_info:
            strategy_test.plan_logic_check('ORIGIN', 2)

class TestStrategyAddActivity(object):
    def test_add_origin_plan(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x, 1)
        assert isinstance(strategy_test.head, Plan)
        assert isinstance(strategy_test.tail, Plan)
        assert strategy_test.head == strategy_test.tail
        assert strategy_test.rank == 1

    def test_add_other_plan_simultaneously(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x, 1)
        strategy_test.add_activity('PICK', lambda x: x, 2)
        strategy_test.add_activity('SWIM', lambda x: x, 3)

        assert isinstance(strategy_test.head, Plan)
        assert isinstance(strategy_test.tail, Plan)
        assert strategy_test.head != strategy_test.tail
        assert strategy_test.rank == 3

        p = 0
        pointer = strategy_test.head
        while(pointer):
            assert pointer.order == p
            p += 1
            pointer = pointer.next_plan

    def test_with_logically_error_plan(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x, 1)

        msg = "Error at line 2: 'ORIGIN' activity must be the first component and cannot be redefined."
        with pytest.raises(LogicalError, match=f"^{msg}$") as exception_info:
            strategy_test.add_activity('ORIGIN', lambda x: x, 2)
            assert strategy_test.rank == 1


class TestStrategyGetActivity(object):
    def test_with_valid_sequence(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x, 1)
        strategy_test.add_activity('PICK', lambda x: x, 2)
        strategy_test.add_activity('PICK', lambda x: x, 3)
        plan_sequences = strategy_test.get_activity()
        assert isinstance(plan_sequences, types.GeneratorType)

        expected_label = ('ORIGIN', 'PICK', 'PICK')
        for activity, label in zip(plan_sequences, expected_label):
            assert isinstance(activity, Plan)
            assert activity.activity == label
            assert isinstance(activity.func, types.FunctionType)

    def test_with_empty_sequence(self):
        strategy_test = Strategy()
        plan_sequences = strategy_test.get_activity()
        assert isinstance(plan_sequences, types.GeneratorType)

        with pytest.raises(StopIteration) as exception_info:
            next_result = next(plan_sequences)

class TestStrategyShowPlan(object):
    def test_with_valid_sequence(self, capsys):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x, 1)
        strategy_test.add_activity('PICK', lambda x: x, 2)
        strategy_test.add_activity('PICK', lambda x: x, 3)

        expected_plans = ("START\n|\n"
                          "A0: `ORIGIN`\n|\n"
                          "A1: `PICK`\n|\n"
                          "A2: `PICK`\n|\n"
                          "END\n")
        strategy_test.show_plan()
        captured = capsys.readouterr()
        result_plans = captured.out
        assert result_plans == expected_plans

    def test_with_empty_sequence(self, capsys):
        strategy_test = Strategy()
        expected_plans = ("START\n|\n"
                          "END\n")
        strategy_test.show_plan()
        captured = capsys.readouterr()
        result_plans = captured.out
        assert result_plans == expected_plans

class TestPlanInitiation(object):
    def test_object_type(self):
        plan_test = Plan('ORIGIN', lambda x: x)
        assert isinstance(plan_test, Plan)
        assert plan_test.activity == 'ORIGIN'
        assert isinstance(plan_test.func, types.FunctionType)
        assert plan_test.order == 0
        assert plan_test.next_plan is None

        plan_test = Plan('PICK', lambda x: x)
        assert isinstance(plan_test, Plan)
        assert plan_test.activity == 'PICK'
        assert isinstance(plan_test.func, types.FunctionType)
        assert plan_test.order is None
        assert plan_test.next_plan is None

    def test_object_representation(self, capsys):
        plan_test = Plan('ORIGIN', lambda x: x)
        print(plan_test)
        expected_print = "A0: `ORIGIN`\n"
        captured = capsys.readouterr()
        result_print = captured.out
        assert result_print == expected_print

        plan_test_extra = Plan('PICK', lambda x: x)
        plan_test.add_link(plan_test_extra)
        print(plan_test_extra)
        expected_print = "A1: `PICK`\n"
        captured = capsys.readouterr()
        result_print = captured.out
        assert result_print == expected_print

        plan_test = Plan('PICK', lambda x: x)
        print(plan_test)
        expected_print = "[Not Assigned]: `PICK`\n"
        captured = capsys.readouterr()
        result_print = captured.out
        assert result_print == expected_print

class TestPlanAddLink(object):
    def test_add_valid_plan(self):
        plan_test_src = Plan('ORIGIN', lambda x: x)
        plan_test_des = Plan('PICK', lambda x: x)
        plan_test_src.add_link(plan_test_des)

        assert plan_test_src.order == 0
        assert plan_test_src.next_plan == plan_test_des
        assert plan_test_des.order == 1

    def test_linking_from_unassigned_plan(self):
        plan_test_src = Plan('PICK', lambda x: x)
        plan_test_des = Plan('PICK', lambda x: x)

        msg = "'Plan' must be a member of 'Strategy' before linked as source."
        with pytest.raises(ObjectTypeError, match=f"^{msg}$") as exception_info:
            plan_test_src.add_link(plan_test_des)
            assert plan_test_src.next_plan is None
            assert plan_test_src.order is None

    def test_add_invalid_object_type(self):
        plan_test_src = Plan('ORIGIN', lambda x: x)
        plan_test_des = 'Plan'

        msg = "'Plan' must be linked with 'Plan' object, not 'str' object."
        with pytest.raises(ObjectTypeError, match=f"^{msg}$") as exception_info:
            plan_test_src.add_link(plan_test_des)
            assert plan_test_src.next_plan is None
