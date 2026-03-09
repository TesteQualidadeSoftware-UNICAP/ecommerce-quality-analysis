# src/cart.py

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        if price <= 0:
            raise ValueError("Preço inválido")

        if quantity <= 0:
            raise ValueError("Quantidade inválida")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def apply_discount(self, discount):
        total = self.calculate_total()

        if discount < 0 or discount > 1:
            raise ValueError("Desconto inválido")

        if discount > 0:
            total = total - (total * discount)

        return total

    def is_empty(self):
        return len(self.items) == 0
