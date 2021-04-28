import user_interface as ui
from contestant import Contestant

class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self):
        ui.new_contestant(Contestant())

    def pick_winner(self):
        #return contestant
        pass

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
