# 1.10.3

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def db_clients(self):
        return f'Клиент: "{self.name}" Баланс: {self.balance} руб'
