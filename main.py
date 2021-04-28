from sweepstake import Sweepstake
from marketing_firm import MarketingFirm
from marketing_firm_creator import MarketingFirmCreator


def run_simulation():
    sweepstake = Sweepstake("Test_sweepstake")
    sweepstake.register_contestant()
    sweepstake.register_contestant()
    sweepstake.register_contestant()
    winner = sweepstake.pick_winner()
    print(winner.first_name)
    print(winner.last_name)
    print(winner.email_address)
    marketing_firm_creator = MarketingFirmCreator()
    marketing_firm = MarketingFirm(marketing_firm_creator.choose_manager_type())
    test = marketing_firm.create_sweepstakes("Test")
    marketing_firm.manager.insert_sweepstakes(test)



run_simulation()
