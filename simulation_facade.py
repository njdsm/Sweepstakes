import user_interface
from sweepstake import Sweepstake


class SweepstakeFacade:
    def __init__(self):
        self.sweepstake = Sweepstake(user_interface.sweepstakes_name())

    def assign_contestant(self):
        self.sweepstake.register_contestant()

    def generate_winner(self):
        winner = self.sweepstake.pick_winner()
        self.sweepstake.announce_winner(winner)

    def print_contestant_info(self, contestant):
        self.sweepstake.print_contestant_info(self.sweepstake.contestants[contestant.registration_number])

