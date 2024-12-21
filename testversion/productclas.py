import random
from datetime import datetime


class Products:
    def __init__(self, product_name, product_quantity, product_cost, product_workday, product_workmonth,product_workyear):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_cost = product_cost
        self.product_workdate = random.randint(1,30)
        self.product_workmonth = random.randint(1,12)
        self.product_workyear = random.randint(2023,2025)

    def apply_discount(self):
        # Создаем дату истечения срока годности
        expiration_date = datetime(self.product_workyear, self.product_workmonth, self.product_workdate)
        current_date = datetime.now()

        # Проверяем, истек ли срок годности
        if current_date > expiration_date:
            # Применяем скидку 25%
            self.product_cost *= 0.75
            return f"Срок годности истек, новая цена со скидкой: {self.product_cost:.2f}"
        else:
            return print("Срок годности еще не истек, скидка не применяется.")

def append_product():
    chose = int(input("Выберите ваш выбор \n1.Изменить данные пользователей. \n2.Добавить продукт. \n3.. \n4.. \n5.. "))


product = Products("Молоко", 10, 100, 15, 12, 2023)

#применение скидки
# result = product.apply_discount()
