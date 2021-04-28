import random
from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager
# This file will hold the function for user interface and prompts


def new_contestant(contestant):
    contestant.first_name = input("First Name:\n: ")
    contestant.last_name = input("Last Name:\n: ")
    contestant.email_address = input("Email Address:\n: ")
    contestant.registration_number = get_random_number()
    return contestant


def get_random_number():
    return random.randrange(100000, 999999)

