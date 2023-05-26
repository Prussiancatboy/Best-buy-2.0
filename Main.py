import products
import store


class MainMenu:

    """This is the main menu for the user,
    it allows them to order various goods"""

    def __init__(self):
        self.product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250,
                             quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250),
            products.NonStockedProduct("Windows License", price=125),
            products.LimitedProduct("Shipping", price=10, quantity=250,
                                    maximum=1)
            ]
        self.best_buy = store.Store(self.product_list)

    def list_interpreter(self):
        """This makes a nice list that can easily be read"""
        lst = self.best_buy.get_all_products()
        blank_str = ""
        counter = 1
        blank_str += "------\n"
        for item, stock, price in lst:
            blank_str += \
                f"{counter}. {item}, Price: ${price}"
            if isinstance(stock, str) is not True:
                blank_str += f", Quantity: {stock}\n"
            else:
                blank_str += f", {stock}\n"
            counter += 1
        blank_str += "------\n"
        return blank_str

    def make_order(self):
        """Takes orders until the user enters an empty text."""
        order_list = []
        while True:
            product_num = input("Which product # do you want? ")
            if not product_num:
                break

            try:
                product_num = int(product_num)
                if product_num < 1 or product_num > len(self.best_buy.products):
                    raise ValueError("Invalid product number. Please try again.")
            except ValueError as error:
                print(str(error))
                continue

            quantity = input("What amount do you want? ")
            indexer = product_num - 1
            try:
                quantity = int(quantity)
                actual_stock = self.best_buy.products[indexer].quantity
                if actual_stock != "Unlimited":
                    if quantity <= 0:
                        raise ValueError("Invalid quantity. Please enter a positive quantity.")
                    elif quantity > actual_stock and actual_stock > 0:
                        raise ValueError(f"Not enough stock, total stock for item is {self.best_buy.products[indexer].quantity}.")

                try:
                    if int(quantity) > int(self.best_buy.products[indexer].maximum):
                        raise ValueError(f"Can't order over {self.best_buy.products[indexer].maximum}")
                except AttributeError:
                    pass


            except ValueError as error:
                print(str(error))
                continue

            product = self.best_buy.products[product_num - 1]
            order_list.append((product, quantity))
            print("Product added to list!")

        try:
            total_price = self.best_buy.order(order_list)
            formatted_price = f"{total_price:.2f}"
            print(f"Order made! Total payment: ${formatted_price}")
        except ValueError as error:
            print(str(error))

    def start(self):
        """This starts the program, and initializes the ui """
        user_input = input(
             "   \nStore Menu\n   ----------   "
             "\n1. List all products in store"
             "\n2. Show total amount in store\n"
             "3. Make an order\n"
             "4. Quit\nPlease choose a number: "
             )

        if int(user_input) == 1:  # List all products in store
            print(self.list_interpreter())
            self.start()

        elif int(user_input) == 2:  # Show total amount in store
            print(
                f"Total of {self.best_buy.get_total_quantity()} "
                f"items in store")
            self.start()

        elif int(user_input) == 3:  # Make an order
            print(self.list_interpreter())
            self.make_order()
            self.start()

        elif int(user_input) == 4:  # Quit
            print("Buh bye")
            quit()


if __name__ == "__main__":
    program = MainMenu()
    program.start()
