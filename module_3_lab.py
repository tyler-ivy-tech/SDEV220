'''
Tyler Howard
module_3_lab.py
Program for accepting vehicle information, storing it in Automobile object, and then printing out that stored data. 
'''

class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type # car, truck, plane, boat, broomstick

class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors # 2 or 4
        self.roof: str = roof # solid or sun roof
    
    def print_info(self) -> None:
        print("=== Automobile Information ===")
        print("Vehicle type: ", self.vehicle_type)
        print("Year: ", self.year)
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Number of doors: ", self.doors)
        print("Type of roof: ", self.roof)
        print("==============================")

def main() -> None:
    vehicle_type: str = input("Enter the vehicle type: ")
    year: int = int(input("Enter the year of the automobile: "))
    make: str = input("Enter the make of the automobile: ")
    model: str = input("Enter the model of the automobile: ")
    doors: int = int(input("Enter the number of doors on the automobile [2 or 4]: "))
    roof: str = input("Enter the type of roof on the automobile [solid or sun roof]: ")
    automobile: Automobile = Automobile(vehicle_type, year, make, model, doors, roof)
    automobile.print_info()

if __name__ == "__main__":
    main()