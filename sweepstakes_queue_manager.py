from data_queue import Queue
from sweepstake import Sweepstake


class SweepstakesQueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstake):
        pass

    def get_sweepstakes(self):
        return Sweepstake()
