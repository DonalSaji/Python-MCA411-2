print("=" * 70)
print("DAIRY CATTLE GROWTH, HEALTH & FEED MANAGEMENT")
print("PROGRAM 1 - PYTHON DATA STRUCTURES")
print("=" * 70)

# TUPLE 
print("\n1. TUPLE - Fixed Cattle Measurements")

# Tuples are ordered and immutable.
measurements = (36.1, 75.3, 89.1)
print("Original tuple:", measurements)
print("Access first measurement:", measurements[0])

# A new tuple is created to demonstrate an update.
measurements = (36.1, 78.5, 92.4)
print("Updated tuple:", measurements)

# Tuple deletion: the complete tuple can be deleted.
old_measurements = (36.1, 75.3, 89.1)
del old_measurements
print("Original tuple was deleted successfully.")


# -------------------- LIST --------------------
print("\n2. LIST - Animal IDs")

animal_ids = ["ANM-00001", "ANM-00002", "ANM-00003"]
print("Original list:", animal_ids)

# Add
animal_ids.append("ANM-00004")
print("After adding ANM-00004 :", animal_ids)

# Update
animal_ids[1] = "ANM-00022"
print("After updating ANM-00002 :", animal_ids)

# Delete
animal_ids.remove("ANM-00003")
print("After deleting ANM-00003 :", animal_ids)

# Access
print("Access first animal ID:", animal_ids[0])

# SET
print("\n3. SET - Unique Cattle Breeds")

breeds = {"Holstein", "Jersey", "Angus"}
print("Original set:", breeds)

# Add
breeds.add("Gir")
print("After adding Gir:", breeds)

# Update (add another item because set elements are not accessed by index)
breeds.update({"Sahiwal"})
print("After adding Sahiwal:", breeds)

# Delete
breeds.discard("Angus")
print("After deleting Angus:", breeds)

# Access/search
print("Is Holstein present?", "Holstein" in breeds)


# DICTIONARY
print("\n4. DICTIONARY - Individual Cattle Record")

cattle = {
    "animal_id": "ANM-00001",
    "breed": "Holstein",
    "sex": "Female",
    "birth_weight": 36.1,
    "health_score": 8,
    "ration_type": "High Energy"
}

print("Original dictionary:")
for key, value in cattle.items():
    print(f"  {key}: {value}")

# Access
print("Access animal ID:", cattle["animal_id"])

# Add
cattle["weight_12m"] = 285.5
print("After adding 12-month weight:", cattle)

# Update
cattle["health_score"] = 9
print("After updating health score:", cattle)

# Delete
del cattle["ration_type"]
print("After deleting ration type:", cattle)

print("\n" + "=" * 70)
print("PROGRAM 1 Part 1 COMPLETED")
print("=" * 70)

#PROGRAM 2: Menu-Driven Dairy Cattle Data Management System
print("\n" + "=" * 70)
print("PROGRAM 1 Part 2 - MENU-DRIVEN DAIRY CATTLE DATA MANAGEMENT SYSTEM")
print("=" * 70)
import re

# list of cattle records (each record is a dictionary) and each record contains 
#a tuple for measurements (birth, 3-month, 12-month weight)
cattle_records = [
    {
        "animal_id": "ANM-00001",
        "breed": "Holstein",
        "sex": "Female",
        "measurements": (36.1, 78.5, 95.2), 
        "health_score": 8,
        "ration_type": "High Energy"
    },
    {
        "animal_id": "ANM-00002",
        "breed": "Jersey",
        "sex": "Female",
        "measurements": (32.4, 70.2, 82.6),
        "health_score": 9,
        "ration_type": "Balanced"
    },
    {
        "animal_id": "ANM-00003",
        "breed": "Sahiwal",
        "sex": "Male",
        "measurements": (34.8, 76.4, 91.5),
        "health_score": 7,
        "ration_type": "High Energy"
    },
    {
        "animal_id": "ANM-00004",
        "breed": "Holstein",
        "sex": "Female",
        "measurements": (37.2, 80.1, 98.3),
        "health_score": 9,
        "ration_type": "Balanced"
    }
]

# Tuple
farm_info = ("Dairy Farm", "Bengaluru", "Karnataka")

# Set
ration_types = {"High Energy", "Balanced", "Low Energy"}


# VALIDATION
def validate_animal_id(animal_id):
    """Validate ID in the format ANM-00001."""
    return bool(re.fullmatch(r"ANM-\d{5}", animal_id))


def validate_cattle_record(record, existing_ids=None):
    """Validate a cattle record before adding it."""
    if existing_ids is None:
        existing_ids = {c["animal_id"] for c in cattle_records}

    if not validate_animal_id(record["animal_id"]):
        raise ValueError("Animal ID must follow the format ANM-00001.")

    if record["animal_id"] in existing_ids:
        raise ValueError("Animal ID already exists.")

    if not record["breed"].strip():
        raise ValueError("Breed cannot be empty.")

    if record["sex"] not in {"Male", "Female"}:
        raise ValueError("Sex must be Male or Female.")

    birth, weight_3m, weight_12m = record["measurements"]

    if birth <= 0 or weight_3m <= 0 or weight_12m <= 0:
        raise ValueError("All weights must be greater than zero.")

    if not 0 <= record["health_score"] <= 10:
        raise ValueError("Health score must be between 0 and 10.")

    if record["ration_type"] not in ration_types:
        raise ValueError("Invalid ration type.")


# DISPLAY
def display_records(records=None):
    if records is None:
        records = cattle_records

    if not records:
        print("\nNo cattle records found.")
        return

    print("\n" + "-" * 105)
    print(f"{'ID':<13}{'Breed':<13}{'Sex':<10}{'Birth Wt':<12}"
          f"{'3-Month Wt':<13}{'12-Month Wt':<14}{'Health':<10}{'Ration':<15}")
    print("-" * 105)

    for cattle in records:
        birth, weight_3m, weight_12m = cattle["measurements"]
        print(f"{cattle['animal_id']:<13}{cattle['breed']:<13}"
              f"{cattle['sex']:<10}{birth:<12.1f}{weight_3m:<13.1f}"
              f"{weight_12m:<14.1f}{cattle['health_score']:<10}"
              f"{cattle['ration_type']:<15}")

    print("-" * 105)


# ADD
def add_cattle():
    print("\n--- ADD NEW CATTLE ---")

    try:
        animal_id = input("Enter animal ID (ANM-00005): ").strip()
        breed = input("Enter breed: ").strip()
        sex = input("Enter sex (Male/Female): ").strip().title()

        birth = float(input("Enter birth weight (kg): "))
        weight_3m = float(input("Enter 3-month weight (kg): "))
        weight_12m = float(input("Enter 12-month weight (kg): "))

        health = int(input("Enter health score (0-10): "))
        ration = input("Enter ration type (High Energy/Balanced/Low Energy): ").strip().title()

        new_cattle = {
            "animal_id": animal_id,
            "breed": breed,
            "sex": sex,
            "measurements": (birth, weight_3m, weight_12m),
            "health_score": health,
            "ration_type": ration
        }

        validate_cattle_record(new_cattle)
        cattle_records.append(new_cattle)
        print("Cattle record added successfully.")

    except ValueError as error:
        print("Validation Error:", error)


# SEARCH
def search_cattle():
    keyword = input("\nEnter Animal ID or Breed to search: ").strip().lower()

    results = [
        cattle for cattle in cattle_records
        if keyword in cattle["animal_id"].lower()
        or keyword in cattle["breed"].lower()
    ]

    if results:
        print(f"\nFound {len(results)} matching record(s):")
        display_records(results)
    else:
        print("No matching cattle found.")


# UPDATE
def update_cattle():
    animal_id = input("\nEnter Animal ID to update: ").strip().upper()

    cattle = next(
        (item for item in cattle_records if item["animal_id"] == animal_id),
        None
    )

    if cattle is None:
        print("Cattle record not found.")
        return

    try:
        print("1. Update health score")
        print("2. Update ration type")
        print("3. Update 12-month weight")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            health = int(input("Enter new health score (0-10): "))
            if not 0 <= health <= 10:
                raise ValueError("Health score must be between 0 and 10.")
            cattle["health_score"] = health

        elif choice == "2":
            ration = input(
                "Enter new ration (High Energy/Balanced/Low Energy): "
            ).strip().title()
            if ration not in ration_types:
                raise ValueError("Invalid ration type.")
            cattle["ration_type"] = ration

        elif choice == "3":
            weight = float(input("Enter new 12-month weight (kg): "))
            if weight <= 0:
                raise ValueError("Weight must be greater than zero.")
            birth, weight_3m, _ = cattle["measurements"]
            cattle["measurements"] = (birth, weight_3m, weight)

        else:
            print("Invalid choice.")
            return

        print("Cattle record updated successfully.")

    except ValueError as error:
        print("Validation Error:", error)


# DELETE
def delete_cattle():
    animal_id = input("\nEnter Animal ID to delete: ").strip().upper()

    for index, cattle in enumerate(cattle_records):
        if cattle["animal_id"] == animal_id:
            del cattle_records[index]
            print("Cattle record deleted successfully.")
            return

    print("Cattle record not found.")


# DATA STRUCTURE DEMONSTRATIONS
def demonstrate_structures():
    print("\n" + "=" * 70)
    print("PYTHON DATA STRUCTURE DEMONSTRATIONS")
    print("=" * 70)

    # Nested data structure
    print("\n1. Nested Dictionary + Tuple:")
    print(cattle_records[0])

    # Set comprehension
    unique_breeds = {cattle["breed"] for cattle in cattle_records}
    print("\n2. Set Comprehension - Unique breeds:")
    print(unique_breeds)

    # List comprehension
    high_health_cattle = [
        cattle["animal_id"]
        for cattle in cattle_records
        if cattle["health_score"] >= 8
    ]
    print("\n3. List Comprehension - Health score >= 8:")
    print(high_health_cattle)

    # Dictionary comprehension
    weight_gain = {
        cattle["animal_id"]: round(
            cattle["measurements"][2] - cattle["measurements"][0], 2
        )
        for cattle in cattle_records
    }
    print("\n4. Dictionary Comprehension - Weight gain:")
    print(weight_gain)

    # Sorting
    sorted_cattle = sorted(
        cattle_records,
        key=lambda cattle: cattle["measurements"][2],
        reverse=True
    )
    print("\n5. Sorting - Highest 12-month weight first:")
    for cattle in sorted_cattle:
        print(cattle["animal_id"], "-", cattle["measurements"][2], "kg")

    # Aggregation
    total_weight = sum(c["measurements"][2] for c in cattle_records)
    average_weight = total_weight / len(cattle_records)
    maximum_weight = max(c["measurements"][2] for c in cattle_records)
    minimum_weight = min(c["measurements"][2] for c in cattle_records)

    print("\n6. Aggregation:")
    print(f"Total 12-month weight: {total_weight:.2f} kg")
    print(f"Average 12-month weight: {average_weight:.2f} kg")
    print(f"Maximum 12-month weight: {maximum_weight:.2f} kg")
    print(f"Minimum 12-month weight: {minimum_weight:.2f} kg")

    # Set operations
    female_breeds = {
        cattle["breed"] for cattle in cattle_records
        if cattle["sex"] == "Female"
    }
    all_breeds = {cattle["breed"] for cattle in cattle_records}

    print("\n7. Set Operations:")
    print("All breeds:", all_breeds)
    print("Available ration types:", ration_types)
    print("Union:", all_breeds | {"Jersey"})
    print("Intersection with {'Holstein', 'Jersey'}:",
          all_breeds & {"Holstein", "Jersey"})
    print("Difference from {'Holstein', 'Jersey', 'Gir'}:",
          all_breeds - {"Holstein", "Jersey", "Gir"})
    print("Female cattle breeds:", female_breeds)

    # Dictionary operations
    sample = cattle_records[0]
    print("\n8. Dictionary Operations:")
    print("Keys:", list(sample.keys()))
    print("Values:", list(sample.values()))
    print("Animal ID using get():", sample.get("animal_id"))
    print("Contains 'breed' key?", "breed" in sample)


# -------------------- MENU --------------------
def menu():
    while True:
        print("\n" + "=" * 70)
        print("DAIRY CATTLE DATA MANAGEMENT SYSTEM")
        print("=" * 70)
        print("1. Display all cattle records")
        print("2. Add new cattle")
        print("3. Search cattle")
        print("4. Update cattle")
        print("5. Delete cattle")
        print("6. Demonstrate data structures and processing")
        print("7. Display farm information")
        print("0. Exit")
        print("=" * 70)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_records()
        elif choice == "2":
            add_cattle()
        elif choice == "3":
            search_cattle()
        elif choice == "4":
            update_cattle()
        elif choice == "5":
            delete_cattle()
        elif choice == "6":
            demonstrate_structures()
        elif choice == "7":
            print("\nFarm Information:")
            print("Farm Name :", farm_info[0])
            print("City      :", farm_info[1])
            print("State     :", farm_info[2])
        elif choice == "0":
            print("\nThank you for using the Dairy Cattle Data Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid menu option.")


if __name__ == "__main__":
    menu()

