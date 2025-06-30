# A simple verison of PyProduct, only with the essential stuff.

class Product:
    def __init__(self, name, price, amountInStock):
        self.name = name
        self.price = price
        self.amountInStock = amountInStock

    def customer_buy(self, amount):
        if self.amountInStock < amount:
            print("Entschuldigung, aber so viel haben wir nicht mehr auf Lager.")
        else:
            self.amountInStock -= amount

    def customer_return(self, amount):
        self.amountInStock += amount

    def owner_restock(self, amount):
        self.amountInStock += amount

productList = [
pc := Product("PC", 249.99, 14),
laptop := Product("Laptop", 199.99, 18),
keyboard := Product("Keyboard", 17.49, 70),
mouse := Product("Mouse", 9.99, 93)
]
productListValidation = []

for product in productList:
    productListValidation.append(product.name.lower())
    print(f"-{product.name} {product.price} $")