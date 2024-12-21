import re

from card import Card

class User:
    user_list = []
    def __init__(self, user_id, surname, firstname, email, phone, cards, admin):
        self.user_id = user_id
        self.surname = surname
        self.firstname = firstname
        self.email = email
        self.phone = phone
        self.cards = cards
        self.basket = []
        self.admin = admin

    @classmethod
    def registration(cls):
        firstname = input("Введите свое имя: ")
        surname = input("Введите свою фамилию: ")
        user_chosepasport_or_phone = input("Выберите что будете регистрировать и введите число одно:\n"
                                           "1. Введите паспорт айди. \n"
                                           "2. Введите номер телефона.\n"
                                           "3. Введите оба: Паспорт айди и номер телефона. Также напоминание: в случае двойной авторизации будет скидка 5% на первую покупку.\n"
                                           "ВВедите свой выбор: ")

        if user_chosepasport_or_phone == '1':
            user_id = input("Введите свой паспортный айди: ")
            phone = None
        elif user_chosepasport_or_phone == '2':
            phone = input("Введите свой номер телефона: ")
            user_id = None
        elif user_chosepasport_or_phone == '3':
            user_id = input("Введите свой паспортный айди: ")
            phone = input("Введите свой номер телефона: ")
        else:
            return print("Введите цифру одну.")


        email = input("Введите вашу почту: ")

        add_card = input("Хотите добавить карту? (да/нет): ").lower()
        cards = []
        if add_card == 'да':
            card_number = input("Введите номер карты: ")
            card_password = input("Введите пароль карты: ")
            card_expiry = input("Введите дату истечения карты (например, 12/25): ")


            new_card = Card(card_number, card_password, card_expiry)
            cards.append(new_card)
            print(f"Карта {new_card} успешно добавлена.")


        new_user = cls(user_id, surname, firstname, email, phone, cards, admin=False)
        cls.user_list.append(new_user)

        print(f"Пользователь {firstname} {surname} успешно зарегистрирован.")

    @classmethod
    def show_users(cls):
        if not cls.user_list:
            print("Нет зарегистрированных пользователей.")
        else:
            for user in cls.user_list:
                card_details = "\n".join(str(card) for card in user.cards)
                print(f"ID: {user.user_id}, Имя: {user.firstname} {user.surname}, Почта: {user.email}, Телефон: {user.phone}\nКарты:\n{card_details}, Админ: {user.admin}")
    @classmethod
    def enter(cls):
        chose_enter = int(input("Выберите один тип регистрации с помощью вашего номера или паспорт айди:\n 1. \n 2."))
        email = int(input("ВВедите свой Email: "))


    @classmethod
    def enters_menu(cls):
        while True:
            try:
                enter = int(input(
                    "ЗДравствуйте добро пожаловать в наш онлайн магазин. Просим вас сначала зарегестрироваться или войти выберите однин вариант. \n 1.Зарегестрироваться. \n2.Войти. \n 3.Выйти из программы.\n ВВедите свой выбор: "))
                if enter == 1:
                    cls.registration()
                if enter == 2:
                    cls.enter()
                if enter == 3:
                    exit()
                else:
                    print("Вы неправильно ввели введите снова число.")
            except ValueError:
                print("Введите числовое значение.")


#Класни текшириб олиш
#User.registration()
#User.show_users()

def user_menu(self):
        user_inp = int(input("Выберите товар"))

def admin_menu(self):
    pass
# def get_admins():
#         if superuser.admin:
#             return admin_menu()
#         else:
#             return user_menu()
