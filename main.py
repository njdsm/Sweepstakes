from simulation_facade import SweepstakeFacade


def run_simulation():
    sweepstake = SweepstakeFacade()
    sweepstake.assign_contestant()
    for contestant in sweepstake.sweepstake.contestants:
        sweepstake.print_contestant_info(sweepstake.sweepstake.contestants[contestant])
    sweepstake.generate_winner()

    # Dependency Injection
    #marketing_firm = MarketingFirm(MarketingFirmCreator())
    #print(marketing_firm.manager)


run_simulation()
