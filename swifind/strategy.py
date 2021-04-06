class Strategy:
    """
    Function sequence handler for each swimmer.
    """

    class Closures:
        """
        Decorator for Strategy Class
        """
        def plan_iterator(func):
            """
            Iterate all connected plan from root.
            """
            def wrapper(obj):
                plan = obj.root
                while(plan):
                    func(obj, plan)
                    plan = plan.next_plan
            return wrapper

    def __init__(self, root=None):
        self.root = Plan('root', URL=root)

    @Closures.plan_iterator
    def show_plan(self, plan=None):
        """
        Show sequence of plan assigned to this strategy.
        """
        print(plan)


    @Closures.plan_iterator
    def execute(self, plan=None):
        """
        Execute registered sequence of plan.
        """
        print(plan)


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
