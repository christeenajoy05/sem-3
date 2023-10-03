def add_lists(list1, list2):
    # Check if the lists have the same length
    if len(list1) != len(list2):
        return None  # Return None if the lists have different lengths

    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result


try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    # Input lists from the user
    list1 = [int(x) for x in input("Enter the elements of the first list separated by spaces: ").split()]
    list2 = [int(x) for x in input("Enter the elements of the second list separated by spaces: ").split()]

    # Call the function to add the lists
    sum_list = add_lists(list1, list2)

    if sum_list is not None:
        print("Result of element-wise addition:", sum_list)
    else:
        print("Lists have different lengths. Cannot perform element-wise addition.")
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")
