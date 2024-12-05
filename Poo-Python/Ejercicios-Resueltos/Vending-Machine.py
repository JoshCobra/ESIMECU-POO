class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f" {self.name} : {str(self.price)}"

    def __repr__(self): # sirve como reemplazo de __str__ y es dirigido mas a lenguaje maquina 
        return str(self)


class VendingMachine: 
    def __init__(self, password):
        self.password = password
        self.balance = 0
        self.items = []

    def add_item(self, item_name, price, password):
        if password != password: 
            print("Incorrect Password")
        else:
            pass

    def purchase_item(self, index, pay):
        pass

    def __str__(self):
        return f"Vending Machine: "


password = "apple"
wrong_pass = "1234" 

vm = VendingMachine(password)

vm.add_item("Oreos", 1.25, password)
vm.add_item("Lays Chips", 1.5, password)
vm.add_item("Coca-Cola", 1.75, wrong_pass)
vm.add_item("Cheetos", 1.50, password)

print(vm)