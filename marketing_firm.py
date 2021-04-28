from sweepstake import Sweepstake


class MarketingFirm:
    # Uses dependency injection. Whatever type of manager is created doesn't matter to the MarketingFirm
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self, name):
        new_sweepstake = Sweepstake(name)
        return new_sweepstake
