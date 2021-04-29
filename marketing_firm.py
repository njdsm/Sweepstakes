from sweepstake import Sweepstake


class MarketingFirm:
    # Uses dependency injection. Whatever type of manager is created doesn't matter to the MarketingFirm
    # By using this no matter which manager type is passed in, their functions will both work off of the same calls,
    # even though they are a little different
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self, name):
        new_sweepstake = Sweepstake(name)
        self.manager.insert_sweepstakes(new_sweepstake)
