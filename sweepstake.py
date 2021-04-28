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
        return self.contestants.get(winner)

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
        print(contestant.registration_number)

    def announce_winner(self, winner):
        for contestant in self.contestants:
            if self.contestants[contestant].registration_number == winner.registration_number:
                self.contestants[contestant].notify("You are the winner!")
            else:
                self.contestants[contestant].notify(f"Congrats to {winner.first_name} {winner.last_name}. "
                                                    f"They won the {self.name} sweepstake!")
