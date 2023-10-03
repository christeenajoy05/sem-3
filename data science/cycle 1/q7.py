def is_armstrong_number(num):
    # Calculate the number of digits in 'num'
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of digits raised to the power of 'num_digits'
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if it's an Armstrong number
    return num == digit_sum


# Iterate through numbers from 1 to 1000 and print Armstrong numbers
print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
for i in range(1, 1001):
    if is_armstrong_number(i):
        print(i,end=" ")

