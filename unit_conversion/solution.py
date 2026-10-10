def convert_units_length(value, from_unit, to_unit):
    # Define conversion factors to meters
    to_meters = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }

    # Convert value to meters first
    value_in_meters = value * to_meters.get(from_unit, 1)

    # Convert from meters to target unit
    return value_in_meters / to_meters.get(to_unit, 1)

def convert_units_weight(value, from_unit, to_unit):
    # Define conversion factors to kilograms
    to_kilograms = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.453592,
        'oz': 0.0283495
    }

    # Convert value to kilograms first
    value_in_kilograms = value * to_kilograms.get(from_unit, 1)

    # Convert from kilograms to target unit
    return value_in_kilograms / to_kilograms.get(to_unit, 1)

def convert_units_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9/5) + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32

    # If the units are the same, return the original value
    return value

def convert_units(value, from_unit, to_unit):
    # Determine the type of conversion based on units
    length_units = {'m', 'km', 'cm', 'mm', 'in', 'ft', 'yd', 'mi'}
    weight_units = {'kg', 'g', 'mg', 'lb', 'oz'}
    temperature_units = {'C', 'F', 'K'}

    if from_unit in length_units and to_unit in length_units:
        return convert_units_length(value, from_unit, to_unit)
    elif from_unit in weight_units and to_unit in weight_units:
        return convert_units_weight(value, from_unit, to_unit)
    elif from_unit in temperature_units and to_unit in temperature_units:
        return convert_units_temperature(value, from_unit, to_unit)
    else:
        raise ValueError("Incompatible units for conversion.")

print("welcome to the Unit Conversion Program!")
print("You can convert between length, weight, and temperature units.")
print("Choose the type of conversion you want to perform:")
print("1. Length")
print("2. Weight")
print("3. Temperature")
choice = input("Enter the number corresponding to your choice: ")
continue_conversion = True
while continue_conversion:
    if choice == '1':
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (m, km, cm, mm, in, ft, yd, mi): ")
        to_unit = input("Enter the unit to convert to (m, km, cm, mm, in, ft, yd, mi): ")
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    elif choice == '2':
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (kg, g, mg, lb, oz): ")
        to_unit = input("Enter the unit to convert to (kg, g, mg, lb, oz): ")
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    elif choice == '3':
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (C, F, K): ")
        to_unit = input("Enter the unit to convert to (C, F, K): ")
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    else:
        print("Invalid choice. Please select 1 for Length, 2 for Weight or 3 for Temperature.")

    continue_choice = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        continue_conversion = False