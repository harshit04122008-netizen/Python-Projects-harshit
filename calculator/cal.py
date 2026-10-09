import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    if x < 0:
        return "Error: Square root of negative number is not allowed."
    return math.hypot(x, 0)

def factorial(x):
    if x < 0:
        return "Error: Factorial of negative number is not defined."
    return math.factorial(x)

def log(x, base=math.e):
    if x <= 0:
        return "Error: Logarithm of non-positive number is not defined."
    return math.log(x, base)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def cot(x):
    if x == 0:
        return "Error: Cotangent of zero is not defined."
    return 1 / math.tan(x)

def sec(x):
    if x == 0:
        return "Error: Secant of zero is not defined."
    return 1 / math.cos(x)

def csc(x):
    if x == 0:
        return "Error: Cosecant of zero is not defined."
    return 1 / math.sin(x)

def deg_to_rad(degrees):
    return math.radians(degrees)

def rad_to_deg(radians):
    return math.degrees(radians)

def sinh(x):
    return math.sinh(x)

def cosh(x):
    return math.cosh(x)

def tanh(x):
    return math.tanh(x)

def coth(x):
    if x == 0:
        return "Error: Hyperbolic cotangent of zero is not defined."
    return 1 / math.tanh(x)

def sech(x):
    if x == 0:
        return "Error: Hyperbolic secant of zero is not defined."
    return 1 / math.cosh(x)

def csch(x):
    if x == 0:
        return "Error: Hyperbolic cosecant of zero is not defined."
    return 1 / math.sinh(x)

print("Calculator Module Loaded. You can now use the functions defined in this module.")
print("Available functions: 1. add, 2. subtract, 3. multiply, 4. divide, 5. power, 6. sqrt, 7. factorial, 8. log, 9. sin, 10. cos, 11. tan, 12. cot, 13. sec, 14. csc, 15. deg_to_rad, 16. rad_to_deg, 17. sinh, 18. cosh, 19. tanh, 20. coth, 21. sech, 22. csch.")
choices = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
    '5': power,
    '6': sqrt,
    '7': factorial,
    '8': log,
    '9': sin,
    '10': cos,
    '11': tan,
    '12': cot,
    '13': sec,
    '14': csc,
    '15': deg_to_rad,
    '16': rad_to_deg,
    '17': sinh,
    '18': cosh,
    '19': tanh,
    '20': coth,
    '21': sech,
    '22': csch
}
choice = input("Enter the number corresponding to the operation you want to perform: ")
if choice in choices:
    if choice in ['1', '2', '3', '4', '5']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = choices[choice](x, y)
    elif choice in ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']:
        x = float(input("Enter the number: "))
        if choice == '8':
            base = input("Enter the base (default is e): ")
            if base:
                base = float(base)
                result = choices[choice](x, base)
            else:
                result = choices[choice](x)
        else:
            result = choices[choice](x)
    print(f"Result: {result}")