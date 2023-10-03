def count_vowels(string):
    # Initialize a dictionary to store the count of each vowel
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the string to lowercase to make it case-insensitive
    string = string.lower()

    # Iterate through the characters in the string
    for char in string:
        if char in vowel_counts:
            # If the character is a vowel, increment its count in the dictionary
            vowel_counts[char] += 1

    return vowel_counts

try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    # Input a string from the user
    input_string = input("Enter a string: ")

    # Call the count_vowels function to count vowels in the string
    result = count_vowels(input_string)

    # Display the counts of each vowel
    for vowel, count in result.items():
        print(f"{vowel}: {count}")
except ValueError:
    print("Invalid input. Please enter a valid string.")
