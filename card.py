import random
class Card:
    def __init__(self, number, password, datetime):
        self.number = number
        self.password = password
        self.datetime = datetime
        self.balance = random.randint(1, 10000)

    def __str__(self):
        return f"Card Number: {self.number}, Expiry: {self.datetime}, Balance: {self.balance}$"

