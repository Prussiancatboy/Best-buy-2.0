class Product:
    """This makes products and does various things like buying, setting stock,
    and checking stock"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """This gets the product quantity and returns it"""
        return self.quantity

    def set_quantity(self, quantity):
        """This gets the product and sets the quantity"""
        self.quantity = quantity

    def is_active(self):
        """This just sends the current state"""
        return self.active

    def activate(self):
        """Activates product"""
        self.active = True

    def deactivate(self):
        """Deactivates product"""
        self.active = False

    def show(self):
        """Shows price, and quantity of a certain product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buys the given quantity of the product"""
        print(self.name, quantity)
        if quantity <= 0:
            raise ValueError("Can only be a positive number.")

        if not self.active:
            raise Exception("Product is inactive.")

        if quantity > self.quantity:
            raise ValueError("Not enough stock.")

        self.quantity -= quantity
        total = self.price * quantity
        return float(total)
