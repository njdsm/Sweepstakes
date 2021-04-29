from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager


def choose_manager_type():
    print("Which type of sweepstakes manager do you want to use?\n"
          "1: Queue (First in First Out)\n2: Stack (Last in First Out)")
    try:
        choice = int(input(":"))
        assert choice == 1 or choice == 2
        if choice == 1:
            return SweepstakesQueueManager()
        else:
            return SweepstakesStackManager()
    except:
        print("Not a valid option")
        choice = self.choose_manager_type()
        return choice

