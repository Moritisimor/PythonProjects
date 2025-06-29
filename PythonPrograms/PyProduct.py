from random import randint

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

paymentMethodList = ["Credit Card", "Debit Card", "PurchaseBuddy", "Bill"]

productList = [
pc := Product("PC", 249.99, 14),
laptop := Product("Laptop", 199.99, 18),
keyboard := Product("Keyboard", 17.49, 70),
mouse := Product("Mouse", 9.99, 93)
]
productListValidation = []

for product in productList:
    productListValidation.append(product.name.lower())

while True: # If the user wants to buy something again, they will get back here.
    for product in productList:
        print(f"- {product.name} {product.price} $")

    while True: # If the user selects a product which does not exist, they'll go back to here.
        productSelection = input("Choose the product you want to buy: ")
        if productSelection.lower() in productListValidation:
            break
        else:
            print("Please choose a valid product.")

    while True: # If the user enters anything which is not an integer, they'll go back to here.
        try:
            productSelectionAmount = int(input("Enter how much you would like to order: "))
            if productSelectionAmount >= 1:
                break
            else:
                print("Can't purchase 0 or less.")
        except ValueError:
            print("Please only enter integers.")

    orderSurname = input("Enter your surname: ")
    orderFirstname = input("Enter your first name: ")
    orderAdress = input("Enter your adress: ")

    while True: # If the user enters a payment method which does not exist, they'll go back to here.
        for paymentMethod in paymentMethodList:
            print(f"- {paymentMethod}")

        orderPaymentMethod = input("Choose your payment method: ")
        if orderPaymentMethod.lower() in (paymentMethod.lower() for paymentMethod in paymentMethodList):
            break
        else:
            print("Please choose one of the payment methods above.")

    orderDeliveryTimeline = f"{randint(2, 3)} Days"

    print("You ordered:")
    print(f"{productSelection} x{productSelectionAmount}\n")
    print("Your delivery adress:")
    print(f"{orderFirstname}, {orderSurname}")
    print(f"{orderAdress} \n")
    print("Your expected delivery timeline:")
    print(f"{orderDeliveryTimeline}\n")
    print("Your Payment method:")
    print(f"{orderPaymentMethod} \n")
    input("Press enter to confirm: ")

    print("Would you like to order something again?")
    again = input("Y/N: ")
    if again.lower() in ["y", "yes"]:
        continue
    else:
        break