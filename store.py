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
            if product.quantity != "Unlimited":
                total += product.quantity
        return total

    def get_all_products(self):
        """This code returns all product names"""
        product_list = []
        staging_list = []
        for product in self.products:
            if product.is_active() is True:
                if product.name not in staging_list:
                    staging_list = [product.name]

                try:
                    if product.maximum > 0:
                        staging_list.append(
                            f"Limited to {product.maximum} per order!")

                        staging_list.append(product.price)
                except AttributeError:
                    staging_list.append(product.quantity)
                    staging_list.append(product.price)
                try:
                    staging_list.append(product.promotion.name)

                except AttributeError:
                    staging_list.append("None")

            # this code makes sure the list isn't blank,
            # and it also keeps duplicates out
            counter = 0
            for lst in staging_list:
                counter += 1
                if counter >= 3:
                    if staging_list not in product_list:
                        product_list.append(staging_list)

        return product_list

    @staticmethod
    def order(shopping_list):
        """Buys the products on the shopping list
        and returns the total price of the order"""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return float(total_price)

    def find_product_by_name(self, name):
        """Finds an active product by its name"""
        for product in self.products:
            if product.name == name and product.is_active():
                return product
