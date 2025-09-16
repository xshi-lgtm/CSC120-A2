from computer import *
from typing import Optional

class ResaleShop:
    inventory: list

    def __init__(self, item_0):
        self.inventory = [item_0]

    def buy(self, computer: Computer):
        self.inventory.append(computer)
        print("Buying",computer.description)
        return self.inventory.index(computer)
    
    def sell(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Computer not found in the inventory.")
    
    def get_inventory(self):
        for item in self.inventory:
            print(f'Item ID {self.inventory.index(item)} : [description: {item.description}], [processor type: {item.processor_type}], [hard drive capacity: {item.hard_drive_capacity}], [memory: {item.memory}], [operating system: {item.operating_system}], [year made: {item.year_made}], [price: {item.price}]')

    def update_price(self, computer: Computer,new_price:int):
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print('Computer not found in inventory.')

    def refurbish(self, computer:Computer, new_os: Optional[str] = None):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 
            elif int(computer.year_made) < 2012:
                computer.price = 250 
            elif int(computer.year_made) < 2018:
                computer.price = 550
            else:
                computer.price = 1000 

            if new_os is not None:
                computer.update_os(new_os)
        else:
            print('Computer not found in inventory.')


item_1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

def main():

    shop: ResaleShop = ResaleShop(item_0)

    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    computer_id = shop.buy(item_1)
    print("Adding to inventory...")
    print("Done\n")

    print("Cheking inventory...")
    shop.get_inventory()
    print("Done\n")

    new_OS = "MacOS Monterey"
    print('Refurbishing Item ID', computer_id, ", updating OS to", new_OS)
    shop.refurbish(item_1, new_OS)
    print("Updating inventory")
    print("Done\n")

    print("Checking inventory...")
    shop.get_inventory()
    print("Done\n")

    new_price = 300
    print("Updating price for Item ID", computer_id, "to", new_price)
    shop.update_price(item_1, new_price)
    print("Updating inventory")
    print("Done\n")

    print("Checking inventory...")
    shop.get_inventory()
    print("Done\n")

    shop.sell(item_1)
    print ("Sold",item_1.description)
    print("Updating inventory")
    print("Done\n")
    

    print("Checking inventory...")
    shop.get_inventory()
    print("Done\n")


if __name__ == "__main__":
    main()
