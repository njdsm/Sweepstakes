class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email_address = ""
        self.registration_number = 0

    def notify(self, is_winner):
        print(is_winner)
