from sweepstake import Sweepstake
from marketing_firm import MarketingFirm
from marketing_firm_creator import MarketingFirmCreator
from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager


def run_simulation():
    sweepstake = Sweepstake("Test_sweepstake")
    sweepstake.register_contestant()
    marketing_firm_creator = MarketingFirmCreator()
    marketing_firm = MarketingFirm(marketing_firm_creator.choose_manager_type())
    test = marketing_firm.create_sweepstakes("Test")
    marketing_firm.manager.insert_sweepstakes(test)
    

run_simulation()
