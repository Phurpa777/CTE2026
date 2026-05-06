'''#part1: counting sort
def counting_sort(arr):
    # Find the maximum value in the array
    max_value = max(arr)
    # Create counting array
    count = [0] * (max_value + 1)
    # Store frequency of each element
    for num in arr:
        count[num] += 1
    # Create sorted array
    sorted_array = []
    # Build the sorted array
    for i in range(len(count)):
        while count[i] > 0:
            sorted_array.append(i)
            count[i] -= 1
    return sorted_array
# Example Usage
arr = [4, 2, 2, 8, 3, 3, 1]

print("Original Array:")
print(arr)
print("Sorted Array:")
print(counting_sort(arr))'''

#part 2
# Radix Sort Implementation using Counting Sort
# Counting Sort function used by Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    # Output array
    output = [0] * n
    # Count array for digits 0-9
    count = [0] * 10
    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    # Change count[i] so it contains actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]
# Radix Sort function
def radix_sort(arr):
    # Find maximum number
    max_value = max(arr)
    # Apply counting sort for every digit
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr
# Example Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original Array:")
print(arr)
print("Sorted Array:")
print(radix_sort(arr))
