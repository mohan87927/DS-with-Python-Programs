import time
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # Choose the last element as the pivot
    
    # Partition the array into sub-arrays
    less = []
    equal = []
    greater = []
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    
    # Recursively sort the sub-arrays
    sorted_less = quicksort(less)
    sorted_greater = quicksort(greater)
    
    # Concatenate the sorted sub-arrays and the pivot element
    return sorted_less + equal + sorted_greater

# Example usage:
arr = [4, 2, 1, 7, 5, 3]
start_time=time.time()
sorted_arr = quicksort(arr)
end_time=time.time()
print(sorted_arr)
print("Time taken:",end_time-start_time,"Seconds")
