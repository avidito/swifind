class Strategy:
    """
    Function sequence handler for each swimmer.
    """
    def __init__(self):
        self.root, self.tail = None, None

    class Decorator:
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

    # Extraction Method
    def add_root_plan(self, url):
        """
        Adding root activity to plan.
        """
        self.root = Plan('root', url=url)
        self.tail = self.root

    def add_collect_plan(self, id, path):
        """
        Adding collect activity to plan.
        """
        p = Plan('collect', id=id, path=path)
        self.tail.add_link(p)
        self.tail = self.tail.next_plan

    @Decorator.plan_iterator
    def show_plan(self, plan=None):
        """
        Show sequence of plan assigned to this strategy.
        """
        print(plan)

    @Decorator.plan_iterator
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
        args = ', '.join((f'{key}={value}' for key, value in self.args.items()))
        return f'{order}: `{self.activity}`. {args}'

    def add_link(self, destination):
        """
        Linking new next plan to this plan.
        """
        self.next_plan = destination
        self.next_plan.order = self.order + 1
