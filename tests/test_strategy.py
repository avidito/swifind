import pytest
import types

from swifind.strategy import Strategy, Plan

class TestStrategyInitiation(object):
    def test_object_type(self):
        strategy_test = Strategy()
        assert isinstance(strategy_test, Strategy)
        assert strategy_test.root is None
        assert strategy_test.tail is None

class TestStrategyAddActivity(object):
    def test_add_origin_plan(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x)
        assert isinstance(strategy_test.root, Plan)
        assert isinstance(strategy_test.tail, Plan)
        assert strategy_test.root == strategy_test.tail

    def test_add_other_plan_simultaneously(self):
        strategy_test = Strategy()
        strategy_test.add_activity('ORIGIN', lambda x: x)
        strategy_test.add_activity('PICK', lambda x: x)
        strategy_test.add_activity('PICK', lambda x: x)

        assert isinstance(strategy_test.root, Plan)
        assert isinstance(strategy_test.tail, Plan)
        assert strategy_test.root != strategy_test.tail

        p = 0
        pointer = strategy_test.root
        while(pointer):
            assert pointer.order == p
            p += 1
            pointer = pointer.next_plan

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

class TestPlanAddLink(object):
    def test_add_valid_plan(self):
        plan_test_src = Plan('ORIGIN', lambda x: x)
        plan_test_des = Plan('PICK', lambda x: x)
        plan_test_src.add_link(plan_test_des)

        assert plan_test_src.order == 0
        assert plan_test_src.next_plan == plan_test_des
        assert plan_test_des.order == 1
