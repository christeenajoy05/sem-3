print("Register No: SJC22MCA2020 \n Name: Christeena Joy \n Batch: MCA 2022-24\n**************************\n")
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_non_prime_in_interval(start, end):
    for num in range(start, end + 1):
        if not is_prime(num):
            print(num, end=" ")

# Define the interval

start=int(input("Enter the lower limit: "))
end=int(input("Enter the upper limit: "))


print("Non-prime numbers in the interval [{}, {}]: ".format(start, end))
print_non_prime_in_interval(start, end)
