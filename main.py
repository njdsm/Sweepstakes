import user_interface
from sweepstake import Sweepstake
from marketing_firm import MarketingFirm
from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager
from marketing_firm_creator import MarketingFirmCreator


def run_simulation():
    sweepstake = Sweepstake("Test_sweepstake")
    sweepstake.register_contestant()
    marketing_firm_creator = MarketingFirmCreator()
    marketing_firm = MarketingFirm(marketing_firm_creator.choose_manager_type())
    print(marketing_firm.manager)




run_simulation()
