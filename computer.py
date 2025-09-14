class Computer:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

item_0 : Computer = Computer('2019 MacBook Pro', 'Intel', 256,  16, 'High Sierra', 2019, 1000)

# def main():
#     print(item_0.description)

# if __name__ == "__main__":
#     main()

    # What methods will you need?