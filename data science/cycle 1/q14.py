def find_absent_digits(mobile_number):
    # Create a set containing all digits from 0 to 9
    all_digits = set(range(10))

    # Convert the mobile number to a set of digits
    mobile_digits = set(map(int, str(mobile_number)))

    # Calculate the absent digits by finding the difference between all_digits and mobile_digits
    absent_digits = all_digits - mobile_digits

    return absent_digits

try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    # Input a 10-digit mobile number from the user
    mobile_number = input("Enter a 10-digit mobile number: ")

    # Check if the input has exactly 10 digits and contains only digits
    if len(mobile_number) == 10 and mobile_number.isdigit():
        mobile_number = int(mobile_number)
        absent_digits = find_absent_digits(mobile_number)

        if not absent_digits:
            print("All digits are present in the mobile number.")
        else:
            print("Digits absent in the mobile number:", sorted(absent_digits))
    else:
        print("Invalid input. Please enter a 10-digit mobile number.")
except ValueError:
    print("Invalid input. Please enter a valid 10-digit mobile number.")
