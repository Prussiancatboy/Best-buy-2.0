
class Store:
    """This code deals with all the products, and manages the inventory"""
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """this code adds products"""
        self.products.append(product)

    def remove_product(self, product):
        """this code removes products"""
        self.products.remove(product)

    def get_total_quantity(self):
        """This code returns the total number of products"""
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self):
        """This code returns all product names"""
        product_list = []
        for product in self.products:
            if product.active is True:
                product_list.append(
                    [product.name, product.quantity, product.price]
                )

        return product_list

    @staticmethod
    def order(shopping_list):
        """Buys the products on the shopping list
        and returns the total price of the order"""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return float(total_price)
