
class Card:
    def __init__(self, number, password, datetime, balance):
        self.number = []
        self.password = []
        self.datetime = []
        self.balance = []

    def __str__(self):
        return f"Номер: {self.number} \n Пароль: {self.password} \n Время работы: {self.datetime} \n Баланс: {self.balance}$"

