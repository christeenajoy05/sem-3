def sum_of_digits(num):
    # Calculate the sum of digits in the number
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    # Input a positive number from the user
    num = int(input("Enter a positive number: "))

    if num <= 0:
        print("Please enter a positive number.")
    else:
        while num > 0:  # Updated condition to check if num is greater than zero
            digit_sum = sum_of_digits(num)
            print(f"{num} - {digit_sum} = {num - digit_sum}")
            num -= digit_sum

except ValueError:
    print("Invalid input. Please enter a valid positive number.")
