# src/order.py

class Order:
    def __init__(self, cart, customer_name, address):
        if cart.is_empty():
            raise ValueError("Não é possível criar pedido com carrinho vazio")

        self.cart = cart
        self.customer_name = customer_name
        self.address = address
        self.status = "created"
        self.total = cart.calculate_total()

    def calculate_shipping(self, state):
        if state == "PE":
            return 20
        elif state in ["PB", "AL", "RN"]:
            return 30
        else:
            return 50

    def apply_coupon(self, coupon_code):
        if coupon_code == "PROMO10":
            self.total *= 0.9
        elif coupon_code == "PROMO20":
            self.total *= 0.8
        else:
            raise ValueError("Cupom inválido")

    def finalize_order(self, payment_confirmed):
        if payment_confirmed:
            self.status = "paid"
        else:
            self.status = "pending"

    def cancel_order(self):
        if self.status == "paid":
            raise Exception("Pedido já pago não pode ser cancelado diretamente")
        self.status = "cancelled"

    def summary(self):
        return {
            "customer": self.customer_name,
            "address": self.address,
            "total": self.total,
            "status": self.status
        }
