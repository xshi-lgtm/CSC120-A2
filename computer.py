"""
   Filename: computer.py
Description: This file defines Computer class, which is an object with attributes of description,
             processor typer, hard drive capacity, memory, operating system, year made, and price.
             Also, the computer class has two methods: updating price and updating system.
     Author: Amy Tang and Cola Shi
       Date: 16 Sep 2025
"""
class Computer: # defines the class with required attributes
    description: str # model name for the computer
    processor_type: str # the processor information of the computer
    hard_drive_capacity: int # the hard drive capacity of the computer
    memory: int # the memory capacity of the computer
    operating_system: str # the current operating system of the computer
    year_made: int # the year the computer is produced 
    price: int # the price the computer is sold

    """
    This constructor takes in a bunch of information for a computer object and initialize its attributes.
    """
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        # set up the computer with given attributes
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    """
    This method updates price for a existing computer.
    """
    def update_price(self, new_price: int):
        self.price = new_price # update the computer's price with a new_price

    """
    This method updates operating system for a existing computer.
    """
    def update_os(self, new_os: str):
        self.operating_system = new_os # update the computer's operating system with new_os

"""
Creates the first Computer object (item_0) with provided information.
"""
item_0 : Computer = Computer('2019 MacBook Pro', 'Intel', 256,  16, 'High Sierra', 2019, 1000)
