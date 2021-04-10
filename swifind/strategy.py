class Strategy:
    """
    Function sequence handler for each swimmer.
    """
    def __init__(self):
        self.root, self.tail = None, None

    class Closure:
        """
        Decorator for Strategy Class
        """
        def plan_iterator(func):
            """
            Iterate all connected plan from root.
            """
            def wrapper(obj):
                plan = obj.origin
                while(plan):
                    obj = func(obj, plan)
                    plan = plan.next_plan
                return obj
            return wrapper

    # Extraction Method
    def add_origin_plan(self, url):
        """
        Adding origin activity to plan.
        """
        self.origin = Plan('origin', url=url)
        self.tail = self.origin

    def add_pick_plan(self, id, path):
        """
        Adding pick activity to plan.
        """
        p = Plan('pick', id=id, path=path)
        self.tail.add_link(p)
        self.tail = self.tail.next_plan

    @Closure.plan_iterator
    def show_plan(self, plan=None):
        """
        Show sequence of plan assigned to this strategy.
        """
        if (plan is None):
            plan = self.root
        print(plan)

    @Closure.plan_iterator
    def execute(self, plan=None):
        """
        Execute registered sequence of plan.
        """
        if (plan is None):
            plan = self.root
        print(plan)

class Plan:
    """
    Object that represent one activity.
    """
    def __init__(self, activity, **kwargs):
        self.activity = activity
        self.args = kwargs
        self.order = None if (activity != 'origin') else 0
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
