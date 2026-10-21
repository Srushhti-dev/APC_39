class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI payment of", amount, "completed.")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card payment of", amount, "completed.")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet payment of", amount, "completed.")


def process_payment(payment, amount):
    payment.make_payment(amount)


for payment in [UPIPayment(), CardPayment(), WalletPayment()]:
    process_payment(payment, 1500)
