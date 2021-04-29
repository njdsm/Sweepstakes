from sweepstake_facade import SweepstakeFacade
from marketing_firm import MarketingFirm
import marketing_firm_creator

def run_simulation():
    # Dependency Injection
    manager = marketing_firm_creator.choose_manager_type()
    marketing_firm = MarketingFirm(manager)
    marketing_firm.create_sweepstakes("test")
    print(marketing_firm.manager)
    print(marketing_firm.manager.get_sweepstakes())







run_simulation()
