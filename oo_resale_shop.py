"""
   Filename: oo_resale_shop.py
Description: This file defines a Resaleshop class that manages the inventory consisiting of computers. 
             This class allows buying new computers (adding new computers to the inventory), 
             selling computers (removing computers from the inventory), updating price for computers, 
             and refurbishing used computers for the computer.
             The inventory is printed everytime an operation is done.
     Author: Amy Tang and Cola Shi
       Date: 16 Sep 2025
"""
from computer import * # Import everything from the file named computer.py
from typing import Optional # Import useful containers from the typing module

class ResaleShop:
    inventory: list # one attribute for the class Resaleshop is the inventory which is a list of Computer objects

    """
    This constructor takes in one computer object and stores in the inventory.
    """
    def __init__(self):
        self.inventory = [] # initialize the inventory with an empty list

    """
    This method adds new computers to the inventory. 
    """
    def buy(self, computer: Computer):
        self.inventory.append(computer) # append the new computer to the list named inventory
        print("Buying",computer.description) # print the description of the new computer
        return self.inventory.index(computer) # returns the index of the new computer in the list
    
    """
    This method removes computers that are sold out from the inventory.
    """
    def sell(self, computer: Computer):
        if computer in self.inventory: # checks if the computer that's being sold is in the inventory
            self.inventory.remove(computer) # remove the computer from the list
        else:
            print("Computer not found in the inventory.") # prints error message if the computer is not in the inventory
    
    """
    This method prints all information of computers in the inventory. 
    """
    def get_inventory(self):
        if self.inventory: # checks if there is computer object in the inventory
            for item in self.inventory: # use for loop to do formatted print
                print(f'Item ID {self.inventory.index(item)} : [description: {item.description}], [processor type: {item.processor_type}], [hard drive capacity: {item.hard_drive_capacity}], [memory: {item.memory}], [operating system: {item.operating_system}], [year made: {item.year_made}], [price: {item.price}]')
        else:
            print("No computers found in inventory.") # prints the error message if there are not computers in the inventory

    """
    This method updates price using methods from the class Computer.
    """
    def update_new_price(self, computer: Computer,new_price:int): # this function needs new price as an input
        if computer in self.inventory: # checks if the computer is in the inventory
            computer.update_price(new_price) # uses the method for the class Computer
        else:
            print('Computer not found in inventory.') # prints error message if the computer is not in the inventory.

    """
    This method refurbish the computer, updates operating system and price for old computers. 
    """
    def refurbish(self, computer:Computer, new_os: Optional[str] = None): # takes in new operating system as an input
        if computer in self.inventory: # checks if there are computers in the inventory
            if int(computer.year_made) < 2000: # locates the year the computer was made and determines the updated price
                computer.price = 0 
            elif int(computer.year_made) < 2012:
                computer.price = 250 
            elif int(computer.year_made) < 2018:
                computer.price = 550
            else:
                computer.price = 1000 

            if new_os is not None: # checks if the input of new operating system is none
                computer.update_os(new_os) # updates the operating system for the computer
        else:
            print('Computer not found in inventory.') # prints an error message if the computer is not in the inventory


item_1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500) # initializes a new computer with given information

def main():

    shop: ResaleShop = ResaleShop()  # starts with an empty inventory
    shop.inventory.append(item_0) # appends a new item to the inventory for the following codes to operate correctly


    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add a new computer to the resale store's inventory
    computer_id = shop.buy(item_1) # access the index of the computer in the inventory
    print("Adding to inventory...")
    print("Done\n")

    # Make sure it worked by checking inventory
    print("Cheking inventory...")
    shop.get_inventory()
    print("Done\n")

    #Refurbishing the computer if needed
    new_OS = "MacOS Monterey"
    print('Refurbishing Item ID', computer_id, ", updating OS to", new_OS)#print the specific information of the refurbished computer
    shop.refurbish(item_1, new_OS)
    print("Updating inventory")
    print("Done\n")

    #Checking the inventory again and print the information of the computers in the inventory
    print("Checking inventory...")
    shop.get_inventory()
    print("Done\n")

    #Updating the price to 300
    new_price = 300
    print("Updating price for Item ID", computer_id, "to", new_price) # print the updated information
    shop.update_new_price(item_1, new_price)
    print("Updating inventory")
    print("Done\n")

    #Check the inventory again to see if the price has changed
    print("Checking inventory...")
    shop.get_inventory()
    print("Done\n")

    #Now, let's sellllll the computer!!!!
    shop.sell(item_1)
    print ("Sold",item_1.description)
    print("Updating inventory")
    print("Done\n")
    
    #Ok, let's check the inventory to see the current information of the computer
    print("Checking inventory...")
    shop.get_inventory()
    print("Done\n")


if __name__ == "__main__":
    main()
