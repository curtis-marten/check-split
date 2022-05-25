class Item:

    owners = []
    
    def __init__(self, name, quantity, price, owners):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.owners = owners


# Define the parts of a basic restaurant check
class Check:

    def __init__(self, items):
        self.title = ""
        self.items = items    # creates a new list of items in the check

    def addItem(self, item):
        self.items.append(item)

    def print(self):
        for i in self.items:
            print(i.name, i.price, i.quantity, i.owners)


itemsList = [Item('steak tacos', 3, 42, []), Item('chicken taco', 1, 12, [])]
itemsList[0].owners = ['Johnny', 'Billy', 'Samantha']
print(itemsList[0].owners)
checkTest = Check(itemsList)

checkTest.print()
checkTest.addItem(Item('carnitas', 17, 1, []))
checkTest.print()
