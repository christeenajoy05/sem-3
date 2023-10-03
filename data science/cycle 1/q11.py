def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    # Input elements from the user
    elements = [int(x) for x in input("Enter elements separated by spaces: ").split()]

    # Call the bubble_sort function to sort the elements
    bubble_sort(elements)

    # Display the sorted elements
    print("Sorted elements:", elements)
except ValueError:
    print("Invalid input. Please enter valid numerical values separated by spaces.")
