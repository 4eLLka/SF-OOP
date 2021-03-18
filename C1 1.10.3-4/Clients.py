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
        return f'Клиент: "{self.name}" Баланс: {self.balance} руб.'


new_Client = Client('Иван Петров', 50)
print(new_Client.db_clients())

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

#1.10.4

class Guest(Client):
    def __init__(self, name, balance, city, status):
        super().__init__(name, balance)
        self.city = city
        self.status = status

    def get_status(self):
        return self.status

    def get_city(self):
        return self.city

    def get_balance(self):
        return self.balance


all_clients = [{'name': 'Иван Петров', 'balance': 50, 'city': 'Москва', 'status': 'Наставник'},
               {'name': 'Семен Слепаков', 'balance': 3500, 'city': 'Самара', 'status': 'Артист'},
               {'name': 'Виталий Жуков', 'balance': 100, 'city': 'Санкт-Петербург', 'status': 'Водитель'},
               {'name': 'Тагир Раимов', 'balance': 0, 'city': 'Казань', 'status': 'Ученик'}]
party_guests = [Guest(p['name'], p['balance'], p['city'], p['status']) for p in all_clients]
for guest in party_guests:
    print(f'"{guest.get_name()}", г.{guest.get_city()}, статус "{guest.get_status()}"')
