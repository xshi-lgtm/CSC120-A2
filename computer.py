class Computer:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_price(self, new_price: int):
        self.price = new_price

    def update_os(self, new_os: str):
        self.operating_system = new_os

item_0 : Computer = Computer('2019 MacBook Pro', 'Intel', 256,  16, 'High Sierra', 2019, 1000)
