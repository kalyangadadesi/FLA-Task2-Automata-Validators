from validators.password import validate_password
from validators.email import validate_email
from validators.atm_pin import validate_pin

def main():
    choices = {
        "1": ("Password", validate_password),
        "2": ("Email", validate_email),
        "3": ("ATM PIN", validate_pin),
    }
    print("FINITE AUTOMATA VALIDATION SYSTEM")
    while True:
        print("\n1. Password verification\n2. Email format validation")
        print("3. ATM PIN verification\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            print("Thank you!")
            break
        if choice not in choices:
            print("Please choose 1, 2, 3 or 4.")
            continue
        name, validator = choices[choice]
        value = input(f"Enter {name}: ")
        valid, message = validator(value)
        print(("ACCEPTED" if valid else "REJECTED") + " - " + message)

if __name__ == "__main__":
    main()
