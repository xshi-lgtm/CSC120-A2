from computer import *
from typing import Optional

class ResaleShop:

    def __init__(self):
        self.inventory = [item_0]
        print("Initially, the shop has:", item_0.description)

    def buy(self, computer: Computer):
        self.inventory.append(computer)
    
    def sell(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
    
    def get_inventory(self):
        for item in self.inventory:
            print(f'Item ID: {self.inventory.index(item)} - [description:{item.description}], [processor type:{item.processor_type}], [hard drive capacity:{item.hard_drive_capacity}], [memory:{item.memory}], [operating system:{item.operating_system}], [year made:{item.year_made}], [price:{item.price}]')

    def update_price(self, new_price:int):
        for item in self.inventory:
            item.price = new_price

    def refurbish(self, new_os: Optional[str] = None):
        for computer  in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os
        # else:
        #     print("Item not found. Please select another item to refurbish.")


item_1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

def main():
    shop: ResaleShop = ResaleShop()

    shop.buy(item_1)
    print("After buying, the shop has:")
    shop.get_inventory()

    shop.sell(item_1)
    print("After selling, the shop has:")
    shop.get_inventory()

    shop.update_price(300)
    print("After updating price, the shop has:")
    shop.get_inventory()

    shop.refurbish("new-os")
    print("After refurbishing, the shop has:")
    shop.get_inventory()

if __name__ == "__main__":
    main()
