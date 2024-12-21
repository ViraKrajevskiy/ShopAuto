import random
from datetime import datetime

class Product:
    def __init__(self, name, count,year_use):
        self.name = name
        self.count = count
        self.date_use = random.randint(1, 31)# кайси кун гача
        self.month_use = random.randint(1,12) #кайси ойгача
        self.year_use = year_use# кайси йилгача сроки
        self.cost = random.randint(1, 600) # нархини генерация килади рандомда

    def discount(self):
        current_date = datetime.now()
        product_date = datetime(self.year_use, self.month_use, self.date_use)

        #Текширув кошилмади хозирча юсерда кошилади текшируйв у админми юсерлигига караб коринади сроки админга
        # факат коринади
        # Проверка на просроченость
        if product_date < current_date:
            print(f"Товар '{self.name}' просрочен!")
            self.cost *= 0.5  # Скидка 50%
            print(f"Новая цена товара '{self.name}': {self.cost}")
        else:
            print(f"Товар '{self.name}' ещё годен.")

    def __str__(self):
        return (f"Название: {self.name}, Количество: {self.count}, "
                f"Срок использования (день/месяц/год): {self.date_use}/{self.month_use}/{self.year_use}, "
                f"Цена: {self.cost}")
