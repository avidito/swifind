class Strategy:
    """
    Function sequence handler for each swimmer.
    """
    def __init__(self, root):
        self.root = Plan('root', URL=root)

    def show_plan(self):
        """
        Show sequence of plan assigned to this strategy.
        """
        plan = self.root
        while(plan):
            print(plan)
            plan = plan.next_plan

class Plan:
    """
    Object that represent one activity.
    """
    def __init__(self, activity, **kwargs):
        self.activity = activity
        self.args = kwargs
        self.order = None if (activity != 'root') else 0
        self.next_plan = None

    def __repr__(self):
        order = '[Not Assigned]' if (self.order is None) else f'Order {self.order}'
        args = ' '.join((f'{key}={value}' for key, value in self.args.items()))
        return f'{order}: `{self.activity}`. {args}'

    def add_link(self, destination):
        """
        Linking new next plan to this plan.
        """
        self.next_plan = destination
