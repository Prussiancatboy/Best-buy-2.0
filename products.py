

class Product:
    """This makes products and does various things like buying, setting stock,
    and checking stock"""
    def __init__(self, name, price, quantity):
        self.name = name

        if price > 0:
            self.price = price
        else:
            try:
                raise ValueError("Invalid price. "
                                 "Please enter a positive price.")

            except ValueError as error:
                print(str(error))

        if isinstance(quantity, str) is True or quantity > 0:
            self.quantity = quantity
        else:
            try:

                raise ValueError("Invalid stock quantity. "
                                 "Please enter a positive quantity.")
            except ValueError as error:
                print(str(error))
                quit()

        self.active = True
        self.promotion = None

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
        if quantity <= 0:
            raise ValueError("Can only be a positive number.")

        if not self.active:
            raise Exception("Product is inactive.")

        if self.quantity != "Unlimited":
            if quantity > self.quantity:
                raise ValueError("Not enough stock.")
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()

        total = self.price * quantity

        try:
            promotion = \
                self.promotion.add_promotion(total, self.price, quantity)

            total = promotion


        except AttributeError:
            pass

        return float(total)

    def set_promotion(self, promotion):
        self.promotion = promotion


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, "Unlimited")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum
