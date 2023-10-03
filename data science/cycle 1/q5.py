import math

def find_quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    # Check if the discriminant is negative (no real roots)
    if discriminant < 0:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(round(real_part, 2), round(imaginary_part, 2))
        root2 = complex(round(real_part, 2), round(-imaginary_part, 2))
        return root1, root2
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return round(root1, 2), round(root2, 2)

# Get coefficients from the user
try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    print("Quadratic Equation: ax^2 + bx + c = 0")
    a = float(input("Enter the coefficient 'a': "))
    b = float(input("Enter the coefficient 'b': "))
    c = float(input("Enter the coefficient 'c': "))

    if a == 0:
        print("This is not a quadratic equation (a cannot be zero).")
    else:
        root1, root2 = find_quadratic_roots(a, b, c)

        if isinstance(root1, complex):
            print(f"The roots of the quadratic equation are complex:")
            print(f"Root 1: {root1.real:.2f} + {root1.imag:.2f}i")
            print(f"Root 2: {root2.real:.2f} - {root2.imag:.2f}i")
        else:
            print(f"The roots of the quadratic equation are real:")
            print(f"Root 1: {root1}")
            print(f"Root 2: {root2}")
except ValueError:
    print("Invalid input. Please enter valid numerical coefficients.")
