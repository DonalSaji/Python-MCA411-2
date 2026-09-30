import re

# CUSTOM EXCEPTION
class InvalidCattleRecord(Exception):
    pass

# VALID RECORD STORAGE
valid_records = []

# REGULAR EXPRESSION PATTERNS 10+ DIFFERENT PATTERNS
patterns = {

    # 1. Animal ID
    "animal_id":
        r"^ANM-\d{5}$",
    # 2. Date
    "date":
        r"^\d{2}-\d{2}-\d{4}$",
    # 3. Time
    "time":
        r"^(?:[01]\d|2[0-3]):[0-5]\d$",
    # 4. Email
    "email":
        r"^[\w.-]+@[\w.-]+\.\w{2,}$",
    # 5. Indian contact number
    "phone":
        r"^[6-9]\d{9}$",
    # 6. Indian PIN code
    "pin":
        r"^[1-9]\d{5}$",
    # 7. Alphanumeric cattle code
    "cattle_code":
        r"^[A-Z0-9]{6,12}$",
    # 8. URL
    "url":
        r"^https?://[\w.-]+(?:/[\w./-]*)?$",
    # 9. Integer
    "integer":
        r"^\d+$",
    # 10. Decimal measurement
    "decimal":
        r"^\d+\.\d+$",
    # 11. Breed name
    "breed":
        r"^[A-Za-z ]+$",
    # 12. Ration type
    "ration":
        r"^[A-Za-z ]+$"
}

# REGEX VALIDATION FUNCTION
def validate_pattern(value, pattern, field):
    if value is None:
        raise ValueError(field + " cannot be None.")
    if value.strip() == "":
        raise ValueError(field + " cannot be empty.")
    if not re.fullmatch(pattern, value):
        raise InvalidCattleRecord(
            "Invalid " + field + " format."
        )
    return True

# 1. ANIMAL ID
def validate_animal_id(value):
    validate_pattern(
        value,
        patterns["animal_id"],
        "Animal ID"
    )
    return value

# 2. DATE
def validate_date(value):
    validate_pattern(
        value,
        patterns["date"],
        "Date"
    )
    return value

# 3. TIME
def validate_time(value):
    validate_pattern(
        value,
        patterns["time"],
        "Time"
    )
    return value

# 4. EMAIL
def validate_email(value):
    validate_pattern(
        value,
        patterns["email"],
        "Email"
    )
    return value

# 5. PHONE NUMBER
def validate_phone(value):
    validate_pattern(
        value,
        patterns["phone"],
        "Phone number"
    )
    return value

# 6. PIN CODE
def validate_pin(value):
    validate_pattern(
        value,
        patterns["pin"],
        "PIN code"
    )
    return value

# 7. ALPHANUMERIC CODE
def validate_cattle_code(value):
    validate_pattern(
        value,
        patterns["cattle_code"],
        "Cattle code"
    )
    return value

# 8. URL
def validate_url(value):
    validate_pattern(
        value,
        patterns["url"],
        "URL"
    )
    return value

# 9. INTEGER
def validate_integer(value):
    validate_pattern(
        value,
        patterns["integer"],
        "Integer value"
    )
    return int(value)

# 10. DECIMAL MEASUREMENT
def validate_decimal(value):
    validate_pattern(
        value,
        patterns["decimal"],
        "Decimal measurement"
    )
    return float(value)

# 11. BREED
def validate_breed(value):
    validate_pattern(
        value,
        patterns["breed"],
        "Breed"
    )
    return value

# 12. RATION
def validate_ration(value):
    validate_pattern(
        value,
        patterns["ration"],
        "Ration type"
    )
    return value

# DATA EXTRACTION
def extract_email(text):
    result = re.findall(
        patterns["email"],
        text
    )
    return result


def extract_phone(text):
    result = re.findall(
        r"\b[6-9]\d{9}\b",
        text
    )
    return result


def extract_animal_id(text):
    result = re.findall(
        r"\bANM-\d{5}\b",
        text
    )
    return result

# CATTLE RECORD VALIDATION
def validate_record(record):

    print("\n======================================")
    print("       VALIDATING CATTLE RECORD")
    print("======================================")

    try:

        # Animal ID
        validate_animal_id(
            record["animal_id"]
        )
        print("Animal ID       : Valid")

        # Date
        validate_date(
            record["date"]
        )
        print("Date            : Valid")

        # Time
        validate_time(
            record["time"]
        )
        print("Time            : Valid")

        # Email
        validate_email(
            record["email"]
        )
        print("Email           : Valid")

        # Phone
        validate_phone(
            record["phone"]
        )
        print("Phone           : Valid")

        # PIN
        validate_pin(
            record["pin"]
        )
        print("PIN Code        : Valid")

        # Cattle Code
        validate_cattle_code(
            record["cattle_code"]
        )
        print("Cattle Code     : Valid")

        # URL
        validate_url(
            record["url"]
        )
        print("URL             : Valid")

        # Weight
        record["weight"] = validate_decimal(
            record["weight"]
        )
        print("Weight          : Valid")

        # Health Score
        record["health_score"] = validate_integer(
            record["health_score"]
        )

        if not 1 <= record["health_score"] <= 10:
            raise ValueError(
                "Health score must be between 1 and 10."
            )

        print("Health Score    : Valid")

        # Breed
        validate_breed(
            record["breed"]
        )
        print("Breed           : Valid")

        # Ration
        validate_ration(
            record["ration"]
        )
        print("Ration Type     : Valid")

        print("\nRecord validation successful.")

        return True

    except KeyError as e:

        print(
            "ERROR - Missing field:",
            e
        )

    except ValueError as e:

        print(
            "ERROR - Value error:",
            e
        )

    except InvalidCattleRecord as e:

        print(
            "ERROR - Validation error:",
            e
        )

    except TypeError as e:

        print(
            "ERROR - Invalid data type:",
            e
        )

    except Exception as e:

        print(
            "ERROR - Unexpected error:",
            e
        )

    return False

# STORE VALID RECORD
def store_record(record):
    if validate_record(record):
        valid_records.append(record)
        print("\nRecord stored successfully.")
    else:
        print("\nInvalid record was NOT stored.")

# DISPLAY RECORDS
def display_records():
    print("\n======================================")
    print("          VALID CATTLE RECORDS")
    print("======================================")
    if len(valid_records) == 0:
        print("No valid records available.")
        return
    for record in valid_records:
        print("\nAnimal ID    :", record["animal_id"])
        print("Breed        :", record["breed"])
        print("Date         :", record["date"])
        print("Time         :", record["time"])
        print("Email        :", record["email"])
        print("Phone        :", record["phone"])
        print("PIN          :", record["pin"])
        print("Cattle Code  :", record["cattle_code"])
        print("URL          :", record["url"])
        print("Weight       :", record["weight"], "kg")
        print("Health Score :", record["health_score"])
        print("Ration       :", record["ration"])

# EXCEPTION DEMONSTRATIONS
def demonstrate_exceptions():

    print("\n======================================")
    print("       EXCEPTION DEMONSTRATIONS")
    print("======================================")

    # 1. ValueError
    try:
        number = int("abc")
    except ValueError:
        print("1. ValueError handled: Invalid integer conversion.")

    # 2. TypeError
    try:
        result = "100" + 50
    except TypeError:
        print("2. TypeError handled: Cannot add string and integer.")

    # 3. IndexError
    try:
        data = ["Cow", "Bull"]
        print(data[5])
    except IndexError:
        print("3. IndexError handled: List index does not exist.")

    # 4. KeyError
    try:
        cattle = {
            "animal_id": "ANM-00001",
            "breed": "Jersey"
        }
        print(cattle["weight"])
    except KeyError:
        print("4. KeyError handled: Dictionary key does not exist.")

    # 5. ZeroDivisionError
    try:
        result = 100 / 0
    except ZeroDivisionError:
        print("5. ZeroDivisionError handled: Cannot divide by zero.")

    # 6. AttributeError
    try:
        animal = "Jersey"
        animal.calculate_weight()
    except AttributeError:
        print("6. AttributeError handled: Method does not exist.")

    # 7. NameError
    try:
        print(unknown_variable)
    except NameError:
        print("7. NameError handled: Variable is not defined.")

    # 8. TypeError with function
    try:
        len(100)
    except TypeError:
        print("8. TypeError handled: Object has no length.")

    # 9. Custom Exception
    try:
        raise InvalidCattleRecord(
            "Cattle health record is invalid."
        )
    except InvalidCattleRecord as e:
        print(
            "9. Custom Exception handled:",
            e
        )

    # 10. ValueError for invalid health score
    try:
        health = 15
        if health > 10:
            raise ValueError(
                "Health score must be between 1 and 10."
            )
    except ValueError as e:
        print(
            "10. ValueError handled:",
            e
        )

# USER INPUT
def create_record():
    print("\n======================================")
    print("       CATTLE REGISTRATION")
    print("======================================")

    record = {}

    try:

        record["animal_id"] = input(
            "Animal ID (ANM-00001): "
        )
        record["date"] = input(
            "Date (DD-MM-YYYY): "
        )
        record["time"] = input(
            "Time (HH:MM): "
        )
        record["email"] = input(
            "Email: "
        )
        record["phone"] = input(
            "Phone number: "
        )
        record["pin"] = input(
            "PIN code: "
        )
        record["cattle_code"] = input(
            "Cattle Code (ABC123): "
        )
        record["url"] = input(
            "Farm URL (https://example.com): "
        )
        record["weight"] = input(
            "Weight (example 350.50): "
        )
        record["health_score"] = input(
            "Health Score (1-10): "
        )
        record["breed"] = input(
            "Breed: "
        )
        record["ration"] = input(
            "Ration Type: "
        )
        store_record(record)
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")
    except Exception as e:
        print(
            "Unexpected input error:",
            e
        )

# MAIN MENU
def main():
    while True:
        print("\n")
        print("=" * 55)
        print("   DAIRY CATTLE DATA VALIDATION SYSTEM")
        print("=" * 55)
        print("1. Register and Validate Cattle")
        print("2. Display Valid Records")
        print("3. Extract Information from Text")
        print("4. Demonstrate Exception Handling")
        print("0. Exit")
        print("=" * 55)
        choice = input(
            "Enter your choice: "
        )
        if choice == "1":
            create_record()
        elif choice == "2":
            display_records()
        elif choice == "3":
            text = input(
                "\nEnter text containing cattle information:\n"
            )
            print("\nExtracted Animal IDs:")
            print(extract_animal_id(text))
            print("\nExtracted Email Addresses:")
            print(extract_email(text))
            print("\nExtracted Phone Numbers:")
            print(extract_phone(text))
        elif choice == "4":
            demonstrate_exceptions()
        elif choice == "0":
            print(
                "\nThank you for using the system."
            )
            break
        else:
            print(
                "Invalid menu choice."
            )
main()