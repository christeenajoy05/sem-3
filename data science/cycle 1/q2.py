def print_fibonacci_numbers(n):
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

# Get the number of Fibonacci numbers to print from the user
try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    n = int(input("Enter the number of Fibonacci numbers to print: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_numbers = print_fibonacci_numbers(n)
        print("The first {} Fibonacci numbers are:".format(n))
        for num in fibonacci_numbers:
            print(num, end=" ")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
