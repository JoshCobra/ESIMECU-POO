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
        if self.password != password: 
            print("Incorrect Password")
        else:
            item = Item(item_name, price)
            self.items.append(item)

    def purchase_item(self, index, pay):
        item = self.items[index]
        if (item.price > pay):
            return (None, pay)
        else: 
            self.balance += item.price 
            change = pay - item.price
            return f" {item}, change: {change}"

    def __str__(self):
        info = "\n Vending Machine Balance: " + str(self.balance) + "\n"
        for item in self.items:
            info += str(item) + "\n"
        return info


password = "apple"
wrong_pass = "1234" 

vm = VendingMachine(password)

vm.add_item("Oreos", 1.25, password)
vm.add_item("Lays Chips", 1.5, password)
vm.add_item("Coca-Cola", 1.75, wrong_pass) #No se agrega por que tiene password incorrecto
vm.add_item("Cheetos", 1.50, password)
vm.add_item("Oreos", 1.25, password)
vm.add_item("Coca-Cola", 1.75, password)

print(vm)

print(vm.purchase_item(0, 1)) # No le alcanza a comprar y le devuelve su cambio 
print(vm.purchase_item(2, 5))
print(vm.purchase_item(4, 23))

print(vm)