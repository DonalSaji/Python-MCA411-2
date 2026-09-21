"""
Custom Module: cattle_utils.py
Contains reusable functions for Dairy Cattle Growth, Health & Feed Management.
"""

import re

farm_info = ("Dairy Farm", "Bengaluru", "Karnataka")
ration_types = {"High Energy", "Balanced", "Low Energy"}


# 1. Validation Function
def validate_animal_id(animal_id):
    return bool(re.fullmatch(r"ANM-\d{5}", animal_id))


def validate_cattle_record(record, existing_ids):
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


# 2. Display Function
def display_records(records):
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


# 3. Search Function
def search_records(cattle_records, keyword):
    results = [
        cattle for cattle in cattle_records
        if keyword.lower() in cattle["animal_id"].lower()
        or keyword.lower() in cattle["breed"].lower()
    ]
    return results


# 4. Calculation / Aggregation Function
def calculate_growth_statistics(cattle_records):
    if not cattle_records:
        return 0, 0, 0, 0
    
    total_weight = sum(c["measurements"][2] for c in cattle_records)
    average_weight = total_weight / len(cattle_records)
    maximum_weight = max(c["measurements"][2] for c in cattle_records)
    minimum_weight = min(c["measurements"][2] for c in cattle_records)
    
    return len(cattle_records), total_weight, average_weight, maximum_weight, minimum_weight


# 5. Business Logic / Processing Function
def calculate_weight_gain(cattle):
    birth, _, weight_12m = cattle["measurements"]
    return round(weight_12m - birth, 2)