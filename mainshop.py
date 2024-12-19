from random import random

from shop import Shop
from user import User
from card import Card
from product import Product

shop = Shop("HUMO","Toshkent Shahar",10000)

user1 = User(12345678,"Akbarxon ","Fayzullayev","akbarxonfayzullayev@gmail.com","+998788889886",True)
user2 = User(87654321,"Kamoliddin ","Kabulov","kamoliddinkabulov@gmail.com","+998788889888",True)
user3 = User(11223344,"Ali ","Valiyev","alivaliyev@gmail.com","+998788889888",False)
user4 = User(44332211,"Nizomiddin ","Jamolov","nizomiddin@gmail.com","+998788889888",False)
user5 = User(12341234,"Alisher ","Navoiy","navoiylegenda@gmail.com","+998788889888",False,)

superuser =[user1,user2,user3,user4,user5]

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

shop.clients.append(user1)
shop.clients.append(user2)
shop.clients.append(user3)
shop.clients.append(user4)
shop.clients.append(user5)

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

# for product in superproduct:
#     print(product)
#     product.discount()
#     print()
#Бу функция текшириш учун чегирмани тест килиш учун факат админ коради нега скидкалигини датасини хам


shop.products.append(product1)
shop.products.append(product2)
shop.products.append(product3)
shop.products.append(product4)
shop.products.append(product5)
shop.products.append(product6)
shop.products.append(product7)
shop.products.append(product8)
shop.products.append(product9)
shop.products.append(product10)

