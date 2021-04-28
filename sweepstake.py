import user_interface as ui
from contestant import Contestant

class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self):
        contestant = ui.new_contestant(Contestant())
        print(contestant.registration_number)

    def pick_winner(self):
        pass

    def print_contestant_info(self):
        pass
