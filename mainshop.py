from shop import Shop
from user import User
from card import Card
from product import Product

shop = Shop("HUMO","Toshkent Shahar",10000)

user1 = User(12345678,"Akbarxon","Fayzullayev","akbarxonfayzullayev@gmail.com","+998788889886",True)
user2 = User(87654321,"Kamoliddin","Kabulov","kamoliddinkabulov@gmail.com","+998788889888",True)
user3 = User(11223344,"Ali","Valiyev","alivaliyev@gmail.com","+998788889888",False)
user4 = User(44332211,"Nizomiddin","Jamolov","nizomiddin@gmail.com","+998788889888",False)
user5 = User(12341234,"Alisher","Navoiy","navoiylegenda@gmail.com","+998788889888",False)

superuser =[user1,user2,user3,user4,user5]
for client in superuser:
    shop.clients.append(client)

card1 = Card(11111111,1111,"14/25")
card2 = Card(22222222,2222,"12/25")
card3 = Card(33333333,3333,"23/25")
card4 = Card(44444444,4444,"09/25")
card5 = Card(55555555,5555,"02/25")

user1.cards.append(card1)
user2.cards.append(card2)
user3.cards.append(card3)
user4.cards.append(card4)
user5.cards.append(card5)

product1 = Product("Olma", 100, 2025)
product2 = Product("Olcha", 100, 2024)
product3 = Product("Anor", 100, 2025)
product4 = Product("Nok", 100, 2025)
product5 = Product("Anjir", 100, 2025)
product6 = Product("Kiwi", 100, 2024)
product7 = Product("Uzum", 100, 2025)
product8 = Product("Apelsin", 100, 2024)
product9 = Product("Limon", 100, 2025)
product10 = Product("Xurmo", 100, 2025)

superproduct = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

for product in superproduct:
    shop.products.append(product)

def main_shop():

    print(f"--'{shop.title}' online do'koniga xush kelibsiz--")
    print("\nXavfsizlik yuzasidan shaxsingizni tasdiqlashingiz lozim. ")
    while True:
        shop.user_register()
        if shop.current_user:
            if not shop.current_user.isadmin:
                while True:
                    status = input("\n1.Mahsulotlar ro'yxatini ko'rish \n2.Mahsulotni sotib olish \n3.Profilni ko'rish \n4.Shaxsiy savatni ko'rish\n5.Registratsiya bo'limiga qaytish:  ")
                    if status == '1':
                        shop.product_list()
                    elif status == '2':
                        shop.buy_func()
                    elif status == '3':
                        shop.current_user_information()
                    elif status == '4':
                        shop.display_user_basket()
                    elif status == '5':
                        break
                    else:
                        print("Noto'g'ri buyruq kiritdingiz. ")
            else:
                print("\n'Admin uchun' bo'limiga kirdingiz. ")
                while True:
                    status1 = input("\n1.Tizmda mavjud mijozlar ro'yxati \n2.Do'kondagi mahsulotlar ro'yxati \n"
                                    "3.Sotuv tarixi \n4.Tizimga mijoz qo'shish\n"
                                    "5.Do'kon balansini ko'rish\n6.Registratsiyaga qaytish. \nBuyruq kiriting: ")
                    if status1 == '1':
                        shop.clients_list()
                    elif status1 == '2':
                        shop.product_list()
                    elif status1 == '3':
                        shop.display_history()
                    elif status1 == '4':
                        shop.add_client()
                    elif status1 == '5':
                        print(f"Do'kon balansi: {shop.balance}$")
                    elif status1 == '6':
                        break
                    else:
                        print("Noto'g'ri buyruq kiritildi. ")

main_shop()
