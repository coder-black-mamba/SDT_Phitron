class Product:
    def __init__(self, name, details, price, stock):
        self.name = name
        self.details = details
        self.price = price
        self.stock = stock


class Shop:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart :) .")

    def add_products(self, arr_of_products):
        for product in arr_of_products:
            self.add_product(product)

    def buy_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if product.stock >= quantity:
                    product.stock = product.stock - quantity
                    print(f"Congrats The {product.name} is avilable . Now Stays {product.stock} In Stock")
                    return
                else:
                    print(f"Only {product.stock} - {product.name} is avilable.")
                    return

        print(f"{product_name} Not Found In Shop :) .")


shopno = Shop("Shopno", "Rajshahi")

p1 = Product("alu", "desi", 20, 5)
p2 = Product("potol", "desi", 30, 7)
p3 = Product("sensation", "bedessi", 50, 8)
p4 = Product("tiger", "bedessi", 60, 9)
p5 = Product("panther", "bedessi", 35, 10)

shopno.add_products([p1, p2, p3, p4, p5])

shopno.buy_product("alu", 2)
shopno.buy_product("alu", 2)
shopno.buy_product("alu", 2)
