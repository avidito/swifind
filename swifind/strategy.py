class Strategy:
    """
    Function sequence handler for each swimmer.
    """
    def __init__(self):
        self.root, self.tail = None, None

    def add_activity(self, label, func):
        """
        Adding activity to strategy plans.
        """
        activity_plan = Plan(label, func)
        if (self.root is None):
            self.root = activity_plan
            self.tail = activity_plan
        else:
            self.tail.add_link(activity_plan)
            self.tail = self.tail.next_plan

    def get_activity(self):
        """
        Move plan pointer and return activity.
        """
        plan_pointer = self.root
        while(plan_pointer):
            yield plan_pointer
            plan_pointer = plan_pointer.next_plan

    def show_plan(self):
        """
        Show sequence of plan assigned to this strategy.
        """
        plan = self.root
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
        order = '[Not Assigned]' if (self.order is None) else f'{self.order}'
        return f'A{order}: `{self.activity}`'

    def add_link(self, destination):
        """
        Linking new next plan to this plan.
        """
        self.next_plan = destination
        self.next_plan.order = self.order + 1
