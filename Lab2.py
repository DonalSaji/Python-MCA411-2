"""
Main Application Script: main.py
Imports and integrates the custom 'cattle_utils' module for Lab 2.
"""

import cattle_utils as cu
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
    }
]


def add_cattle_flow():
    print("\n--- ADD NEW CATTLE ---")
    try:
        animal_id = input("Enter animal ID (ANM-00004): ").strip()
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

        existing_ids = {c["animal_id"] for c in cattle_records}
        cu.validate_cattle_record(new_cattle, existing_ids)
        
        cattle_records.append(new_cattle)
        print("Cattle record added successfully using custom module validation!")

    except ValueError as error:
        print("Validation Error:", error)


def search_cattle_flow():
    keyword = input("\nEnter Animal ID or Breed to search: ").strip()
    results = cu.search_records(cattle_records, keyword)
    
    if results:
        print(f"\nFound {len(results)} matching record(s):")
        cu.display_records(results)
    else:
        print("No matching cattle found.")


def report_statistics_flow():
    print("\n--- FARM GROWTH STATISTICS & REPORTING ---")
    count, total, avg, max_w, min_w = cu.calculate_growth_statistics(cattle_records)
    print(f"Total Cattle Count     : {count}")
    print(f"Total 12-Month Weight  : {total:.2f} kg")
    print(f"Average 12-Month Weight: {avg:.2f} kg")
    print(f"Maximum 12-Month Weight: {max_w:.2f} kg")
    print(f"Minimum 12-Month Weight: {min_w:.2f} kg")


def show_weight_gains_flow():
    print("\n--- INDIVIDUAL WEIGHT GAINS (Business Logic) ---")
    for c in cattle_records:
        gain = cu.calculate_weight_gain(c)
        print(f"ID: {c['animal_id']} ({c['breed']}) -> Total Weight Gain (Birth to 12M): {gain} kg")


# --- Main Menu ---
def main():
    while True:
        print("\n" + "=" * 70)
        print("DAIRY CATTLE MANAGEMENT SYSTEM - LAB 2 (CUSTOM MODULES)")
        print("=" * 70)
        print("1. Display all cattle records (Module function)")
        print("2. Add new cattle (Module validation)")
        print("3. Search cattle (Module search)")
        print("4. View growth statistics & reporting (Module aggregation)")
        print("5. View individual weight gains (Module business logic)")
        print("6. Display Farm Information")
        print("0. Exit")
        print("=" * 70)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            cu.display_records(cattle_records)
        elif choice == "2":
            add_cattle_flow()
        elif choice == "3":
            search_cattle_flow()
        elif choice == "4":
            report_statistics_flow()
        elif choice == "5":
            show_weight_gains_flow()
        elif choice == "6":
            print("\nFarm Information:")
            print("Farm Name :", cu.farm_info[0])
            print("City      :", cu.farm_info[1])
            print("State     :", cu.farm_info[2])
        elif choice == "0":
            print("\nThank you for using the Dairy Cattle Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid menu option.")


if __name__ == "__main__":
    main()