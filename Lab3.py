from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Animal(ABC):

    def __init__(self, animal_id, name, breed):
        self.animal_id = animal_id
        self.name = name
        self.breed = breed

    @abstractmethod
    def calculate_growth(self):
        pass


# CATTLE CLASS - Inherits Animal
class Cattle(Animal):

    def __init__(self, animal_id, name, breed, weight):
        super().__init__(animal_id, name, breed)

        self.__weight = weight       # Private attribute
        self._health_score = 5       # Protected attribute

    # Getter
    def get_weight(self):
        return self.__weight

    # Setter
    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            print("Invalid weight.")

    # Getter
    def get_health_score(self):
        return self._health_score

    # Setter
    def set_health_score(self, score):
        if 1 <= score <= 10:
            self._health_score = score
        else:
            print("Health score must be between 1 and 10.")

    # Method overriding
    def calculate_growth(self):
        return self.__weight * 0.10

    # Magic method
    def __str__(self):
        return (
            f"ID: {self.animal_id}, "
            f"Name: {self.name}, "
            f"Breed: {self.breed}, "
            f"Weight: {self.__weight} kg, "
            f"Health: {self._health_score}"
        )

    # Magic method
    def __eq__(self, other):
        return self.animal_id == other.animal_id

    # Magic method
    def __lt__(self, other):
        return self.__weight < other.get_weight()



# DAIRY CATTLE CLASS
# Multilevel inheritance:
# Animal -> Cattle -> DairyCattle
class DairyCattle(Cattle):

    def __init__(self, animal_id, name, breed, weight, milk_production):
        super().__init__(animal_id, name, breed, weight)
        self.milk_production = milk_production

    # Method overriding
    def calculate_growth(self):
        growth = self.get_weight() * 0.15
        return growth

    def display_milk(self):
        print("Milk Production:", self.milk_production, "litres/day")


# FEED CLASS
class Feed:

    def __init__(self, feed_name, quantity):
        self.feed_name = feed_name
        self.quantity = quantity

    def __str__(self):
        return f"{self.feed_name} - {self.quantity} kg"

# FARM CLASS
# Composition / Aggregation
class Farm:

    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.cattle_list = []
        self.feed_list = []

    # Add cattle object
    def add_cattle(self, cattle):
        self.cattle_list.append(cattle)

    # Add feed object
    def add_feed(self, feed):
        self.feed_list.append(feed)

    # Search cattle
    def search_cattle(self, animal_id):
        for cattle in self.cattle_list:
            if cattle.animal_id == animal_id:
                return cattle

        return None

    # Magic method
    def __len__(self):
        return len(self.cattle_list)

    def display_cattle(self):
        if len(self.cattle_list) == 0:
            print("No cattle records available.")
            return
        print("\n========== CATTLE RECORDS ==========")
        for cattle in self.cattle_list:
            print(cattle)
            if isinstance(cattle, DairyCattle):
                cattle.display_milk()


# CLASS METHODS AND STATIC METHODS

class CattleManager:

    total_cattle = 0

    # Class method
    @classmethod
    def create_cattle(cls, animal_id, name, breed, weight):
        cls.total_cattle += 1
        return Cattle(
            animal_id,
            name,
            breed,
            weight
        )

    # Static method
    @staticmethod
    def validate_animal_id(animal_id):
        return (
            len(animal_id) == 9
            and animal_id.startswith("ANM-")
            and animal_id[4:].isdigit()
        )

# OVERLOADING-LIKE BEHAVIOUR
def feed_cattle(cattle, quantity=5, feed_name="Green Grass"):
    print(
        cattle.name,
        "received",
        quantity,
        "kg of",
        feed_name
    )

# INPUT FUNCTIONS
def get_weight():
    while True:
        try:
            weight = float(input("Enter weight (kg): "))
            if weight > 0:
                return weight
            print("Weight must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def get_health_score():
    while True:
        try:
            score = int(input("Enter health score (1-10): "))
            if 1 <= score <= 10:
                return score
            print("Health score must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

# ADD CATTLE
def add_cattle(farm):
    print("\n========== ADD CATTLE ==========")
    animal_id = input("Enter Animal ID (ANM-00001): ").upper()
    if not CattleManager.validate_animal_id(animal_id):
        print("Invalid Animal ID.")
        return
    if farm.search_cattle(animal_id):
        print("Animal ID already exists.")
        return
    name = input("Enter cattle name: ")
    if name == "":
        print("Name cannot be empty.")
        return
    breed = input("Enter breed: ")
    if breed == "":
        print("Breed cannot be empty.")
        return
    weight = get_weight()
    cattle = CattleManager.create_cattle(
        animal_id,
        name,
        breed,
        weight
    )
    health = get_health_score()
    cattle.set_health_score(health)
    farm.add_cattle(cattle)
    print("Cattle added successfully.")

# UPDATE CATTLE
def update_cattle(farm):
    print("\n========== UPDATE CATTLE ==========")
    animal_id = input("Enter Animal ID: ").upper()
    cattle = farm.search_cattle(animal_id)
    if cattle is None:
        print("Cattle not found.")
        return
    print("\nCurrent Details:")
    print(cattle)
    new_weight = get_weight()
    cattle.set_weight(new_weight)
    new_health = get_health_score()
    cattle.set_health_score(new_health)
    print("Cattle record updated successfully.")

# SEARCH
def search_cattle(farm):
    print("\n========== SEARCH CATTLE ==========")
    animal_id = input("Enter Animal ID: ").upper()
    cattle = farm.search_cattle(animal_id)
    if cattle:
        print("\nCattle Found:")
        print(cattle)
        print(
            "Expected Growth:",
            round(cattle.calculate_growth(), 2),
            "kg"
        )
    else:
        print("Cattle not found.")

# DEMONSTRATE POLYMORPHISM
def demonstrate_polymorphism():
    print("\n========== POLYMORPHISM ==========")
    cattle1 = Cattle(
        "ANM-10001",
        "Cow A",
        "Jersey",
        250
    )
    cattle2 = DairyCattle(
        "ANM-10002",
        "Cow B",
        "Holstein",
        300,
        18
    )
    animals = [cattle1, cattle2]
    for animal in animals:
        print(animal.name)
        print(
            "Calculated Growth:",
            round(animal.calculate_growth(), 2),
            "kg"
        )

# SORT CATTLE
def sort_cattle(farm):
    if len(farm) == 0:
        print("No cattle records available.")
        return
    print("\n========== SORTED CATTLE ==========")
    sorted_cattle = sorted(farm.cattle_list)
    for cattle in sorted_cattle:
        print(cattle)

# MAIN PROGRAM
farm = Farm("Green Dairy Farm")
while True:
    print("\n")
    print("=" * 55)
    print("       DAIRY CATTLE MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Cattle")
    print("2. Display All Cattle")
    print("3. Search Cattle")
    print("4. Update Cattle")
    print("5. Feed Cattle")
    print("6. Sort Cattle by Weight")
    print("7. Demonstrate Polymorphism")
    print("8. Display Number of Cattle")
    print("0. Exit")
    print("=" * 55)
    choice = input("Enter your choice: ")
    if choice == "1":
        add_cattle(farm)
    elif choice == "2":
        farm.display_cattle()
    elif choice == "3":
        search_cattle(farm)
    elif choice == "4":
        update_cattle(farm)
    elif choice == "5":
        if len(farm) == 0:
            print("No cattle available.")
        else:
            animal_id = input("Enter Animal ID: ").upper()
            cattle = farm.search_cattle(animal_id)
            if cattle:
                # Default values
                feed_cattle(cattle)
                # User-defined values
                quantity = float(
                    input("Enter feed quantity (kg): ")
                )
                feed_name = input("Enter feed name: ")
                feed_cattle(
                    cattle,
                    quantity,
                    feed_name
                )
            else:
                print("Cattle not found.")
    elif choice == "6":
        sort_cattle(farm)
    elif choice == "7":
        demonstrate_polymorphism()
    elif choice == "8":
        print(
            "Total cattle in",
            farm.farm_name,
            ":",
            len(farm)
        )
    elif choice == "0":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid choice. Please try again.")