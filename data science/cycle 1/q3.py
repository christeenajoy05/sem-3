def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or c == a:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# Get the side lengths from the user
try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    a = float(input("Enter the length of side 'a': "))
    b = float(input("Enter the length of side 'b': "))
    c = float(input("Enter the length of side 'c': "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid input. Side lengths must be positive numbers.")
    else:
        triangle_type = classify_triangle(a, b, c)
        print(f"The given triangle is a {triangle_type}.")
except ValueError:
    print("Invalid input. Please enter valid side lengths as positive numbers.")
