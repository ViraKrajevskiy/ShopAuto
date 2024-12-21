from user import User
from card import Card

class Shop:
    def __init__(self,title,location,balance):
        self.title = title
        self.location = location
        self.clients = []
        self.products = []
        self.balance = balance
        self.history_sell = []
        self.current_user = None

    def display_user_basket(self):
        if not self.current_user.basket:
            print("Savatchangiz bo'sh!")
            return

        print("\n--Sizning savatchangizdagi mahsulotlar--")
        total_cost = 0
        for idx, item in enumerate(self.current_user.basket, start=1):
            product_name = item['product']
            quantity = item['quantity']
            total_price = item['total_cost']
            total_cost += total_price
            print(f"{idx}. Mahsulot: {product_name} | Miqdor: {quantity} | Umumiy narx: {total_price}$")

        print(f"\nJami narx: {total_cost}$")

    def add_client(self):
        user_id = input("Passport seriyangizni kiriting: ")
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
        email = input("Emailngizni kiriting: ")
        telefon = input("Telefon raqamingizni kiriting: ")
        new_client = User(user_id,ism,familiya,email,telefon,False)
        card = input("Karta raqamingizni kiriting: ")
        password = input("Parolini kiriting: ")
        datetime = input("Kartangizni muddatini kiriting: ")
        new_card = Card(card,password,datetime)
        self.clients.append(new_client)
        new_client.cards.append(new_card)
        print("Tizimga saqlandi. ")

    def display_history(self):
        if not self.history_sell:
            print("Hech qanday xarid amalga oshirilmagan.")
            return

        print("\n--- Xaridlar tarixi ---")
        for index, sale in enumerate(self.history_sell, start=1):
            print(f"{index}. Mahsulot: {sale['product']}")
            print(f"   Miqdor: {sale['quantity']}")
            print(f"   Jami narx: {sale['total_cost']}$")
            print("-----------------------")

    def clients_list(self):
        for idx, client in enumerate(self.clients,start=1):
            print(f"{idx}.{client.surname} {client.firstname} - user_id: {client.user_id} , {client.email} , {client.phone} ")
            print("Kartalari:")
            for card in client.cards:
                print(f"{card.number} - muddat:{card.datetime} , balance: {card.balance}$")
            print("-----------------------")

    def product_list(self):
        if not self.products:
            print("Online do'konda mahsulotlar mavjud emas. ")
        for index, product in enumerate(self.products,start=1):
            print(f"{index}.{product.name}  -  miqdor: {product.count}, ({product.year_use}), {product.cost}$")


    def user_register(self):
        while True:
            status = input("1.Passport ID orqali tizimga kirish 2.Email orqali tizimga kirish: ")
            if status == '2':
                email = input("Emailingizni kiriting: ")
                for client in self.clients:
                    if client.email == email:
                        self.current_user = client
                        return "Tizimga kirish muvaffaqiyatli amalga oshirildi. "
                else:
                    print("Tizimda bunday email ga ega mijoz mavjud emas. ")

            elif status == '1':
                user_id = input("User ID ni kiriting: ")
                if user_id.isdigit():
                    for client in self.clients:
                        if client.user_id == int(user_id):
                            self.current_user = client
                            return "Tabriklaymiz,Tizmimizda mavjud ekansiz Do'kondan mahsulotlar xarid qilishingiz mumkin. "
                    else:
                        print("Tizimda bunday ID li mijoz yo'q yoki kiritilgan ID xato.Iltimios to'g'ri ID kiriting yoki Ro'yxatdan o'ting. ")
                else:
                    print("User ID si faqat sonlarda kiritishi kerak. ")
            elif status == '3':
                break
            else:
                print("Bunday buyruq mavjud emas")

    def buy_func(self):
        status = input("1.Mahsulot xarid qilish 0.Ortga: ")
        if status == '1':
            if not self.products:
                print("Mahsulotlar ro'yxati bo'sh!")
                return

            cart = []

            while True:
                print("\nMahsulotlar ro'yxati:")
                for index, product in enumerate(self.products, start=1):
                    print(f"{index}. {product.name} - miqdor: {product.count}, ({product.year_use}), {product.cost}$")

                try:
                    status_product = int(input("Xarid qilmoqchi bo'lgan mahsulotingizni raqamini yozing: "))
                    if 1 <= status_product <= len(self.products):
                        selected_product = self.products[status_product - 1]

                        miqdor = int(input(f"{selected_product.name} dan nechta sotib olmoqchisiz? "))
                        if miqdor > selected_product.count:
                            print("Uzr, bu miqdorda mahsulot mavjud emas.")
                            continue

                        total_cost = miqdor * selected_product.cost
                        cart.append({
                            'product': selected_product,
                            'quantity': miqdor,
                            'cost': total_cost
                        })
                        print(f"{miqdor} dona {selected_product.name} savatchaga qo'shildi. Umumiy narx: {total_cost}$")

                        status_product2 = input(
                            "1. Yana xarid qilish\n2. To'lovni amalga oshirish\nTanlovingizni kiriting: ")
                        if status_product2 == '1':
                            continue
                        elif status_product2 == '2':
                            total_payment = sum(item['cost'] for item in cart)
                            print(f"\nUmumiy to'lov: {total_payment}$")

                            if not self.current_user.cards:
                                print("Karta mavjud emas! Xarid amalga oshirilmaydi.")
                                return

                            print("Kartalar:")
                            for idx, card in enumerate(self.current_user.cards, start=1):
                                print(f"{idx}. {card}")


                            card_choice = None
                            attempts_card = 3
                            while attempts_card > 0:
                                try:
                                    card_choice = int(
                                        input("Qaysi kartadan to'lovni amalga oshirmoqchisiz? (raqamini kiriting): "))
                                    if 1 <= card_choice <= len(self.current_user.cards):
                                        break
                                    else:
                                        print("Noto'g'ri karta tanlandi.")
                                except ValueError:
                                    print("Iltimos, karta raqamini to'g'ri kiriting.")
                                attempts_card -= 1
                                if attempts_card == 0:
                                    print("Kartani tanlashda 3 ta urinishda ham xato kiritildi. Xarid amalga oshirilmadi.")
                                    return
                                else:
                                    print(f"Yana {attempts_card} urinish qoldi.")

                            selected_card = self.current_user.cards[card_choice - 1]


                            attempts_password = 3
                            while attempts_password > 0:
                                password = input("Karta paroloni kiriting: ")
                                if password.isdigit():
                                    if int(password) == selected_card.password:
                                        print(f"Kartangizda {selected_card.balance}$ mavjud.")
                                        if selected_card.balance >= total_payment:
                                            selected_card.balance -= total_payment

                                            for item in cart:
                                                self.current_user.basket.append({
                                                    'product': item['product'].name,
                                                    'quantity': item['quantity'],
                                                    'total_cost': item['cost']
                                                })

                                            for item in cart:
                                                item['product'].count -= item['quantity']
                                                self.history_sell.append({
                                                    'product': item['product'].name,
                                                    'quantity': item['quantity'],
                                                    'total_cost': item['cost']
                                                })
                                            self.balance += total_payment
                                            print("To'lov muvaffaqiyatli amalga oshirildi. Do'kon balansi yangilandi.")
                                            break

                                        else:
                                            print("Karta balansida yetarli mablag' mavjud emas!")
                                            return
                                    else:
                                        print("Parol noto'g'ri kiritildi.")
                                else:
                                    print("Parol faqat raqamlarda kiritilishi kerak.")
                                attempts_password -= 1
                                if attempts_password == 0:
                                    print(
                                        "Karta parolini kiritishda 3 ta urinishda ham xato kiritildi. Xarid amalga oshirilmadi.")
                                    return
                                else:
                                    print(f"Yana {attempts_password} urinish qoldi.")
                            break
                    else:
                        print("Kiritilgan raqam mahsulotlar ro'yxatida mavjud emas.")
                except ValueError:
                    print("Iltimos, raqam kiriting.")
        elif status == '0':
            return
        else:
            print("Xato buyruq kiritildi. ")
    def current_user_information(self):
        print(f"\nIsmi: {self.current_user.firstname} \nFamiliyasi: {self.current_user.surname}\n"
              f"Emaili: {self.current_user.email}\nTelefon raqami: {self.current_user.phone}\n")
        for card in self.current_user.cards:
            print(f"Kartalari:\n{card.number} - parol: {card.password} ,muddati: {card.datetime} , balansi: {card.balance}$")
            return