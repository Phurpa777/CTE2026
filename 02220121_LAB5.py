'''#task 1
def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons
# Example given in question
arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

index, comparisons = sequential_search(arr, target)

print("List:", arr)
print("Searching for", target, "using Sequential Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)'''
#task 2

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1

    return -1, comparisons


# Binary Search (Recursive)

def binary_search_recursive(arr, target, left, right, comparisons=0):

    if left > right:
        return -1, comparisons

    mid = (left + right) // 2
    comparisons += 1

    if arr[mid] == target:
        return mid, comparisons
    
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right, comparisons)
    
    else:
        return binary_search_recursive(arr, target, left, mid-1, comparisons)


# Example given in question
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67


# Iterative result
index1, comp1 = binary_search_iterative(arr, target)

print("Binary Search (Iterative)")
print("Sorted List:", arr)
print("Searching for", target, "using Binary Search")

if index1 != -1:
    print("Found at index", index1)
else:
    print("Not found")

print("Number of comparisons:", comp1)



# Recursive result
index2, comp2 = binary_search_recursive(arr, target, 0, len(arr)-1)

print("\nBinary Search (Recursive)")

if index2 != -1:
    print("Found at index", index2)
else:
    print("Not found")

print("Number of comparisons:", comp2)