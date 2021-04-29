import user_interface
from marketing_firm import MarketingFirm
import marketing_firm_creator


class SweepstakeFacade:
    def __init__(self):
        # Dependency Injection
        manager = marketing_firm_creator.choose_manager_type()
        self.marketing_firm = MarketingFirm(manager)

    def simulation(self):
        run = True
        while run:
            user_interface.prompt()
            choice = input(": ")
            if choice == "1":
                self.create_sweepstake()
            elif choice == "2":
                self.assign_contestant()
            elif choice == "3":
                self.generate_winner()
            elif choice == "4":
                run = False
            else:
                print("Not a valid option")

    def create_sweepstake(self):
        self.marketing_firm.create_sweepstakes(user_interface.sweepstakes_name())

    def assign_contestant(self):
        sweepstake = self.marketing_firm.manager.get_sweepstakes()
        sweepstake.register_contestant()
        self.marketing_firm.manager.insert_sweepstakes(sweepstake)

    def generate_winner(self):
        sweepstake = self.marketing_firm.manager.get_sweepstakes()
        winner = sweepstake.pick_winner()
        sweepstake.announce_winner(winner)


    def print_contestant_info(self, contestant):
        sweepstake = self.marketing_firm.manager.get_sweepstakes()
        for contestant in sweepstake.contestants:
            sweepstake.print_contestant_info(contestant)
        self.marketing_firm.manager.insert_sweepstakes(sweepstake)

