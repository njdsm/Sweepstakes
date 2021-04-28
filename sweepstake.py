import user_interface as ui
from contestant import Contestant
import random


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self):
        contestant = ui.new_contestant(Contestant())
        if contestant.registration_number in self.contestants.keys():
            self.register_contestant()
        self.contestants[contestant.registration_number] = contestant

    def pick_winner(self):
        keys = list(self.contestants)
        winner = random.randrange(0, len(keys))
        winner = keys[winner]
        print(winner)
        return self.contestants.get(winner)

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
