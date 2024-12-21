
import random
import re

from card1 import Card
from mainshopfunc import user_menu,admin_menu

class User(Card):
    def __init__(self, user_id, username, surname, email, phone, admin, number, password, datetime, balance):
        super().__init__(number, password, datetime, balance)
        self.user_id = user_id
        self.username = username
        self.surname = surname
        self.email = email
        self.phone = phone
        self.basket = []
        self.admin = admin
        self.is_logged_in = False


users = [User("AD213312","Erny","Brun","asxewtry@gmail.com",231223212,False,1270800643488430,2313,"28/24",0)
    ,User("AD3645234", "Vira", "Krajevskiy", "azazel@gmail.com", 952014052, True, 1866237019623388, 2314, "12/25", 0)
]


def menu():
    while True:
        try:
            user_inp = int(input(
                "Здравствуйте! Это приложение для онлайн-продаж. Сначала зарегистрируйтесь или войдите, если у вас уже есть аккаунт.\n"
                "1. Зарегистрироваться.\n"
                "2. Войти.\n"
                "Введите свой выбор: "
            ))
            if user_inp == 1:
                registration()
                break
            elif user_inp == 2:
                enter()
                break
            else:
                print("Вы ввели неправильное число. Попробуйте ещё раз.")
        except ValueError:
            print("Ошибка! Введите число, а не букву.")


def enter():

    email_enter = input("Введите свой email: ")
    user_option = int(input(
        "Выберите, с помощью чего вы хотите войти:\n"
        "1. С помощью номера телефона.\n"
        "2. С помощью паспорта ID.\n"
        "Введите свой выбор: "
    ))

    if user_option == 1:
        phone_enter = int(input("Введите номер телефона: "))
        for user in users:
            if user.email == email_enter and user.phone == phone_enter and user.admin == False:
                print(f"Пользователь {user.username} успешно вошёл в систему!")
                return user_menu()
            elif user.email == email_enter and user.phone == phone_enter and user.admin == True:
                print(f"Добро пожаловать {user.username}")
                return admin_menu()  # Теперь admin_menu работает
        print("Неверные email или номер телефона.")
    elif user_option == 2:
        passport_enter = input("Введите паспорт ID: ")
        for user in users:
            if user.email == email_enter and user.user_id == passport_enter and user.admin == False:
                print(f"Пользователь {user.username} успешно вошёл в систему!")
                return user_menu()
            if user.email == email_enter and user.user_id == passport_enter and user.admin == True:
                print(f"Добро пожаловать {user.username}")
                return admin_menu()
    else:
        return menu()

def registration():

    print("Регистрация пользователя:")

    while True:
        email = input("Введите email: ")
        if re.match(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$', email):
            break
        print("Некорректный email. Попробуйте снова.")


    username = input("Введите имя: ")
    surname = input("Введите фамилию: ")

    print("Выберите способ регистрации: \n1. Только паспортный ID.\n2. Только номер телефона.\n3. Оба (паспортный ID и номер телефона). Скидка 5% на первую покупку при двойной авторизации.")

    user_id, phone = None, None
    while True:
        user_choice = input("Введите ваш выбор (1, 2 или 3): ")

        if user_choice == '1':
            user_id = input("Введите ваш паспортный ID: ")
            break
        elif user_choice == '2':
            while True:
                phone = input("Введите ваш номер телефона: ")
                if re.match(r'^\d{10,15}$', phone):
                    break
                print("Некорректный номер телефона. Попробуйте снова.")
            break
        elif user_choice == '3':
            user_id = input("Введите ваш паспортный ID: ")
            while True:
                phone = input("Введите ваш номер телефона: ")
                if re.match(r'^\d{10,15}$', phone):
                    break
                print("Некорректный номер телефона. Попробуйте снова.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


    cards = []
    if input("Хотите добавить карту? (да/нет): ").strip().lower() == 'да':
        while True:
            card_number = input("Введите номер карты: ")
            if re.match(r'^\d{16}$', card_number):
                break
            print("Некорректный номер карты. Попробуйте снова.")

        card_password = input("Введите пароль карты: ")

        while True:
            card_expiry = input("Введите срок действия карты (например, 12/25): ")
            if re.match(r'^(0[1-9]|1[0-2])/\d{2}$', card_expiry):
                break
            print("Некорректная дата истечения. Попробуйте снова.")

        try:
            new_card = Card(card_number, card_password, card_expiry)
            cards.append(new_card)
            print(f"Карта с номером {card_number} успешно добавлена.")
        except Exception as e:
            print(f"Ошибка при добавлении карты: {e}")

    new_user = User(user_id, username, surname, email, phone, False, None, None, None, 0)
    users.append(new_user)
    print(f"Пользователь {username} успешно зарегистрирован!")
    return menu()

menu()

