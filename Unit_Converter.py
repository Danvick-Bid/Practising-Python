def unit_converter():
    print("Options: 1. Temperature (C to F), 2. Distance (Km to Miles)")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value}°C = {value * 9/5 + 32}°F")
    elif choice == "2":
        print(f"{value} Km = {value * 0.621371} Miles")
    else:
        print("Invalid choice!")

unit_converter()
