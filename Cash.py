class CashRegister:

    TAX_DECIMAL = 0.05

    def __init__(self, cashier):
        self.items = {}
        self.cashier = cashier

    def add_item(self, item, quantity=1):
        self.items[item["name"]] = {
            "price": item["price"],
            "quantity": quantity
        }

    def remove_item(self, item):
        del self.items[item]

    def show_items(self):
        print(self.items)

    def update_price(self, item, new_price):
        self.items[item]["price"] = new_price

    def find_subtotal(self):
        subtotal = 0
        for item_info in self.items.values():
            subtotal += item_info["price"] * item_info["quantity"]
        return subtotal

    def print_subtotal(self):
        print(self.find_subtotal())

    def find_tax(self):
        return round(self.find_subtotal() * CashRegister.TAX_DECIMAL, 2)

    def print_tax(self):
        print(f"Taxes: {self.find_tax()}")

    def find_total(self):
        return round(self.find_subtotal() + self.find_tax(), 2)

    def print_total(self):
        print(f"Total: {self.find_total()}")

    def clear_item(self):
        self.items.clear()


my_cash_register = CashRegister("Nora")
item1 = {"name": "pizza", "price": 3.54}
item2 = {"name": "chocolate", "price": 6.32}
item3 = {"name": "pasta", "price": 2.31}

my_cash_register.add_item(item1)
my_cash_register.add_item(item2, 3)
my_cash_register.add_item(item3, 10)

my_cash_register.show_items()

my_cash_register.remove_item("pizza")
my_cash_register.show_items()

my_cash_register.update_price("pasta", 5.67)
my_cash_register.show_items()

my_cash_register.print_subtotal()
my_cash_register.print_tax()
my_cash_register.print_total()

my_cash_register.clear_item()
my_cash_register.show_items()