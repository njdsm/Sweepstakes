from sweepstake import Sweepstake


class MarketingFirm:
    # Uses dependency injection. Whatever type of manager is created doesn't matter to the MarketingFirm
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        new_sweepstake = Sweepstake(input("Sweepstake name:\n: "))
        return new_sweepstake
