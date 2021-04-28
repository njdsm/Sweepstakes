import email_test_fuction


class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email_address = ""
        self.registration_number = 0

    def notify(self, message, sweepstake_name):
        fullname = self.first_name + self.last_name
        email_test_fuction.email_contestants(self.email_address, message, sweepstake_name, fullname)
        print(message)
