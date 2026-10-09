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

def log10(x):
    if x <= 0:
        return "Error: Logarithm of non-positive number is not defined."
    return math.log10(x)

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

def area_of_circle(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    return math.pi * radius ** 2

def perimeter_of_circle(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    return 2 * math.pi * radius

def area_of_rectangle(length, width):
    if length < 0 or width < 0:
        return "Error: Length and width cannot be negative."
    return length * width

def perimeter_of_rectangle(length, width):
    if length < 0 or width < 0:
        return "Error: Length and width cannot be negative."
    return 2 * (length + width)

def area_of_triangle(base, height):
    if base < 0 or height < 0:
        return "Error: Base and height cannot be negative."
    return 0.5 * base * height

def perimeter_of_triangle(side1, side2, side3):
    if side1 < 0 or side2 < 0 or side3 < 0:
        return "Error: Sides cannot be negative."
    return side1 + side2 + side3

def area_of_square(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return side ** 2

def perimeter_of_square(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return 4 * side

def area_of_parallelogram(base, height):
    if base < 0 or height < 0:
        return "Error: Base and height cannot be negative."
    return base * height

def perimeter_of_parallelogram(side1, side2):
    if side1 < 0 or side2 < 0:
        return "Error: Sides cannot be negative."
    return 2 * (side1 + side2)

def area_of_trapezoid(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        return "Error: Bases and height cannot be negative."
    return 0.5 * (base1 + base2) * height

def perimeter_of_trapezoid(side1, side2, base1, base2):
    if side1 < 0 or side2 < 0 or base1 < 0 or base2 < 0:
        return "Error: Sides and bases cannot be negative."
    return side1 + side2 + base1 + base2

def area_of_rhombus(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        return "Error: Diagonals cannot be negative."
    return 0.5 * diagonal1 * diagonal2

def perimeter_of_rhombus(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return 4 * side

def area_of_kite(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        return "Error: Diagonals cannot be negative."
    return 0.5 * diagonal1 * diagonal2

def perimeter_of_kite(side1, side2):
    if side1 < 0 or side2 < 0:
        return "Error: Sides cannot be negative."
    return 2 * (side1 + side2)

def area_of_ellipse(semi_major_axis, semi_minor_axis):
    if semi_major_axis < 0 or semi_minor_axis < 0:
        return "Error: Axes cannot be negative."
    return math.pi * semi_major_axis * semi_minor_axis

def perimeter_of_ellipse(semi_major_axis, semi_minor_axis):
    if semi_major_axis < 0 or semi_minor_axis < 0:
        return "Error: Axes cannot be negative."
    # Approximation of the perimeter of an ellipse
    h = ((semi_major_axis - semi_minor_axis) ** 2) / ((semi_major_axis + semi_minor_axis) ** 2)
    return math.pi * (semi_major_axis + semi_minor_axis) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

def area_of_sector(radius, angle_in_degrees):
    if radius < 0 or angle_in_degrees < 0:
        return "Error: Radius and angle cannot be negative."
    return (angle_in_degrees / 360) * math.pi * radius ** 2

def perimeter_of_sector(radius, angle_in_degrees):
    if radius < 0 or angle_in_degrees < 0:
        return "Error: Radius and angle cannot be negative."
    arc_length = (angle_in_degrees / 360) * 2 * math.pi * radius
    return arc_length + 2 * radius

def area_of_segment(radius, angle_in_degrees):
    if radius < 0 or angle_in_degrees < 0:
        return "Error: Radius and angle cannot be negative."
    area_of_sector = (angle_in_degrees / 360) * math.pi * radius ** 2
    area_of_triangle = 0.5 * radius ** 2 * math.sin(math.radians(angle_in_degrees))
    return area_of_sector - area_of_triangle

def perimeter_of_segment(radius, angle_in_degrees):
    if radius < 0 or angle_in_degrees < 0:
        return "Error: Radius and angle cannot be negative."
    arc_length = (angle_in_degrees / 360) * 2 * math.pi * radius
    chord_length = 2 * radius * math.sin(math.radians(angle_in_degrees / 2))
    return arc_length + chord_length    

def area_of_cylinder(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    return 2 * math.pi * radius * (radius + height)

def perimeter_of_cylinder(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    return 2 * math.pi * radius * height

def volume_of_cylinder(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    return math.pi * radius ** 2 * height

def surface_area_of_cylinder(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    return 2 * math.pi * radius * (radius + height)

def area_of_cone(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def perimeter_of_cone(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * slant_height

def volume_of_cone(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    return (1 / 3) * math.pi * radius ** 2 * height

def surface_area_of_cone(radius, height):
    if radius < 0 or height < 0:
        return "Error: Radius and height cannot be negative."
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def area_of_sphere(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    return 4 * math.pi * radius ** 2

def perimeter_of_sphere(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    return 2 * math.pi * radius

def volume_of_sphere(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    return (4 / 3) * math.pi * radius ** 3

def surface_area_of_sphere(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    return 4 * math.pi * radius ** 2

def area_of_cube(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return 6 * side ** 2

def perimeter_of_cube(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return 12 * side

def volume_of_cube(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return side ** 3

def surface_area_of_cube(side):
    if side < 0:
        return "Error: Side cannot be negative."
    return 6 * side ** 2

def area_of_cuboid(length, width, height):
    if length < 0 or width < 0 or height < 0:
        return "Error: Length, width, and height cannot be negative."
    return 2 * (length * width + length * height + width * height)

def perimeter_of_cuboid(length, width, height):
    if length < 0 or width < 0 or height < 0:
        return "Error: Length, width, and height cannot be negative."
    return 4 * (length + width + height)

def volume_of_cuboid(length, width, height):
    if length < 0 or width < 0 or height < 0:
        return "Error: Length, width, and height cannot be negative."
    return length * width * height

def surface_area_of_cuboid(length, width, height):
    if length < 0 or width < 0 or height < 0:
        return "Error: Length, width, and height cannot be negative."
    return 2 * (length * width + length * height + width * height)

def area_of_prism(base_area, height):
    if base_area < 0 or height < 0:
        return "Error: Base area and height cannot be negative."
    return base_area * height

def perimeter_of_prism(base_perimeter, height):
    if base_perimeter < 0 or height < 0:
        return "Error: Base perimeter and height cannot be negative."
    return base_perimeter * height

def volume_of_prism(base_area, height):
    if base_area < 0 or height < 0:
        return "Error: Base area and height cannot be negative."
    return base_area * height

def surface_area_of_prism(base_area, base_perimeter, height):
    if base_area < 0 or base_perimeter < 0 or height < 0:
        return "Error: Base area, base perimeter, and height cannot be negative."
    return 2 * base_area + base_perimeter * height

def area_of_pyramid(base_area, height):
    if base_area < 0 or height < 0:
        return "Error: Base area and height cannot be negative."
    return (1 / 3) * base_area * height

def perimeter_of_pyramid(base_perimeter, height):
    if base_perimeter < 0 or height < 0:
        return "Error: Base perimeter and height cannot be negative."
    return (1 / 3) * base_perimeter * height

def  volume_of_pyramid(base_area, height):
    if base_area < 0 or height < 0:
        return "Error: Base area and height cannot be negative."
    return (1 / 3) * base_area * height



print("Calculator Module Loaded. You can now use the functions defined in this module.")
print("Available functions: 1. add, \n 2. subtract,\n 3. multiply,\n 4. divide,\n 5. power,\n 6. sqrt,\n 7. factorial,\n 8. log,\n 9. sin,\n 10. cos,\n 11. tan,\n 12. cot,\n 13. sec,\n 14. csc,\n 15. deg_to_rad,\n 16. rad_to_deg,\n 17. sinh,\n 18. cosh,\n 19. tanh,\n 20. coth,\n 21. sech,\n 22. csch ,\n 23. area_of_circle,\n 24. perimeter_of_circle,\n 25. area_of_rectangle,\n 26. perimeter_of_rectangle,\n 27. area_of_triangle,\n 28. perimeter_of_triangle,\n 29. area_of_square,\n 30. perimeter_of_square,\n 31. area_of_parallelogram,\n 32. perimeter_of_parallelogram,\n 33. area_of_trapezoid, \n 34. perimeter_of_trapezoid,\n 35. area_of_rhombus,\n 36. perimeter_of_rhombus,\n 37. area_of_kite,\n 38. perimeter_of_kite,\n 39. area_of_ellipse, \n 40. perimeter_of_ellipse,\n 41. area_of_sector, \n 42. perimeter_of_sector, \n 43. area_of_segment, \n 44. perimeter_of_segment,\n 45. area_of_cylinder,\n 46. perimeter_of_cylinder,\n 47. volume_of_cylinder,\n 48. surface_area_of_cylinder,\n 49. area_of_cone,\n 50. perimeter_of_cone,\n 51. volume_of_cone,\n 52. surface_area_of_cone,\n 53. area_of_sphere,\n 54. perimeter_of_sphere,\n 55. volume_of_sphere,\n 56. surface_area_of_sphere,\n 57. area_of_cube,\n 58. perimeter_of_cube,\n 59. volume_of_cube,\n 60. surface_area_of_cube ,\n 61.area_of_cuboid ,\n 62.perimeter_of_cuboid ,\n 63.volume_of_cuboid , \n 64.surface_area_of_cuboid , \n 65.area_of_prism , \n 66.perimeter_of_prism , \n 67.volume_of_prism , \n 68.surface_area_of_prism , \n 69.area_of_pyramid , \n 70.perimeter_of_pyramid , \n 71.volume_of_pyramid")
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
    '22': csch,
    '23': area_of_circle,
    '24': perimeter_of_circle,
    '25': area_of_rectangle,
    '26': perimeter_of_rectangle,
    '27': area_of_triangle,
    '28': perimeter_of_triangle,
    '29': area_of_square,
    '30': perimeter_of_square,
    '31': area_of_parallelogram,
    '32': perimeter_of_parallelogram,
    '33': area_of_trapezoid,
    '34': perimeter_of_trapezoid,
    '35': area_of_rhombus,
    '36': perimeter_of_rhombus,
    '37': area_of_kite,
    '38': perimeter_of_kite,
    '39': area_of_ellipse,
    '40': perimeter_of_ellipse,
    '41': area_of_sector,
    '42': perimeter_of_sector,
    '43': area_of_segment,
    '44': perimeter_of_segment,
    '45': area_of_cylinder,
    '46': perimeter_of_cylinder,
    '47': volume_of_cylinder,
    '48': surface_area_of_cylinder,
    '49': area_of_cone,
    '50': perimeter_of_cone,
    '51': volume_of_cone,
    '52': surface_area_of_cone,
    '53': area_of_sphere,
    '54': perimeter_of_sphere,
    '55': volume_of_sphere,
    '56': surface_area_of_sphere,
    '57': area_of_cube,
    '58': perimeter_of_cube,
    '59': volume_of_cube,
    '60': surface_area_of_cube,
    '61': area_of_cuboid,
    '62': perimeter_of_cuboid,
    '63': volume_of_cuboid,
    '64': surface_area_of_cuboid,
    '65': area_of_prism,
    '66': perimeter_of_prism,
    '67': volume_of_prism,
    '68': surface_area_of_prism,
    '69': area_of_pyramid,
    '70': perimeter_of_pyramid,
    '71': volume_of_pyramid
}
choice = input("Enter the number corresponding to the operation you want to perform: ")
again = 'y'
while again.lower() == 'y':

    if choice in choices:
        func = choices[choice]
        num_args = func.__code__.co_argcount #finds the number of arguments the function takes
        args = []
        for i in range(num_args):
            arg = float(input(f"Enter argument {i + 1}: "))
            args.append(arg)
        result = func(*args)
    print(f"The result is: {result}")
    again = input("Do you want to perform another operation? (y/n): ")
print("Thank you for using the calculator module. Goodbye!")