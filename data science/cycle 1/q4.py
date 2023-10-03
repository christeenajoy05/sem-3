def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    gcd = calculate_gcd(a, b)
    return gcd == 1

try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 <= 0 or num2 <= 0:
        print("Invalid input. Please enter positive integers.")
    else:
        if are_coprime(num1, num2):
            print(f"{num1} and {num2} are coprime.")
        else:
            print(f"{num1} and {num2} are not coprime.")
except ValueError:
    print("Invalid input. Please enter valid positive integers.")
