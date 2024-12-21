from card import Card

class User:
    def __init__(self, user_id,firstname,surname, email, phone,isadmin):
        self.user_id = user_id
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.cards = []
        self.basket = []
        self.isadmin = isadmin

    def add_card(self, card: Card):
        self.cards.append(card)
        print(f"Karta {card.number} qo'shildi.")

    def add_to_basket(self, product):
        self.basket.append(product)
        print(f"{product.name} savatga qo'shildi.")

    def clear_basket(self):
        self.basket.clear()
        print("Savat bo'shatildi.")

