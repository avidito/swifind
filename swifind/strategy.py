from .interpreter.exception import SwiplValidationError

LOGIC_CHECK = {
    'ORIGIN': [
        lambda st, act: st.rank == 0,
    ],
    'PICK': [
        lambda st, act: True,
    ],
}

class Strategy:
    """
    Function sequence handler for each swimmer.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.rank = 0

    def plan_logic_check(self, activity):
        """
        Check logical validity of plan addition.
        """
        for check in LOGIC_CHECK[activity]:
            if check(self, activity) == False:
                msg = f"Logical Error from `{activity}` activity."
                raise SwiplValidationError(msg)

    def add_activity(self, activity, func):
        """
        Adding activity to strategy plans.
        """
        self.plan_logic_check(activity)

        activity_plan = Plan(activity, func)
        if (self.head is None):
            self.head = activity_plan
            self.tail = activity_plan
        else:
            self.tail.add_link(activity_plan)
            self.tail = self.tail.next_plan

    def get_activity(self):
        """
        Move plan pointer and return activity.
        """
        plan_pointer = self.head
        while(plan_pointer):
            yield plan_pointer
            plan_pointer = plan_pointer.next_plan

    def show_plan(self):
        """
        Show sequence of plan assigned to this strategy.
        """
        plan = self.head
        print("START\n|")
        while(plan):
            print(f"{plan}\n|")
            plan = plan.next_plan
        print("END")

class Plan:
    """
    Object that represent one activity.
    """
    def __init__(self, activity, func):
        self.activity = activity
        self.func = func
        self.order = None if (activity != 'ORIGIN') else 0
        self.next_plan = None

    def __repr__(self):
        order = '[Not Assigned]' if (self.order is None) else f'A{self.order}'
        return f'{order}: `{self.activity}`'

    def add_link(self, destination):
        """
        Linking new next plan to this plan.
        """
        self.next_plan = destination
        self.next_plan.order = self.order + 1
