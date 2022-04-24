class Item:
    discount = 0.8  # 20 % discount on price
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # validate inputs
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"

        # Assign attributes while initialising object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append all objects to class
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def discount_on_price(self, discount):
        # Global discount attribute of class is used
        self.price = self.price * self.discount
        # self.price = self.price * discount # Discount attribute of object is used

    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


item1 = Item("laptop", 400, 5)
item2 = Item("phone", 1000, 3)

item2.discount_on_price(discount=0.5)
print(item2.price)

# To print all instances of class manually
# for instance in Item.all:
#     print(f"Item ('{instance.name}', {instance.price}, {instance.quantity})")

# To print all instances of call using inbuilt methods
print(Item.all)
