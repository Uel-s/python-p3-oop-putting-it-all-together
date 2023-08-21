class ShoppingCart:
    def __init__(self, coupon=0):
        self.coupon = coupon

    def checkout(self):
        total = sum([item.price for item in self.shopping_cart()])
        total -= total * self.coupon / 100
        return total

client=ShoppingCart("23%")
discount = client.checkout
print(getattr(client,"coupon"))        