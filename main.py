from marketing_firm_creator import MarketingFirmCreator
from marketing_firm import MarketingFirm
from sweepstake import Sweepstake


def run_simulation():
    sweepstake = Sweepstake("Test")
    sweepstake.register_contestant()
    sweepstake.register_contestant()
    winner = sweepstake.pick_winner()
    sweepstake.announce_winner(winner)
    sweepstake.print_contestant_info(winner)
    marketing_firm = MarketingFirm(MarketingFirmCreator().choose_manager_type())
    print(marketing_firm.manager)



run_simulation()
