"""
LAB EXERCISE - 1
PROGRAM 1: Demonstration of Python Data Structures
Domain: Dairy Cattle Growth, Health & Feed Management

Demonstrates:
- Tuple
- List
- Set
- Dictionary
- Add, update, delete and access elements
"""

print("=" * 65)
print("DAIRY CATTLE GROWTH, HEALTH & FEED MANAGEMENT")
print("PROGRAM 1 - PYTHON DATA STRUCTURES")
print("=" * 65)

# -------------------- TUPLE --------------------
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
print("After adding:", animal_ids)

# Update
animal_ids[1] = "ANM-00022"
print("After updating:", animal_ids)

# Delete
animal_ids.remove("ANM-00003")
print("After deleting:", animal_ids)

# Access
print("Access first animal ID:", animal_ids[0])


# -------------------- SET --------------------
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


# -------------------- DICTIONARY --------------------
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

print("\n" + "=" * 65)
print("PROGRAM 1 COMPLETED")
print("=" * 65)
