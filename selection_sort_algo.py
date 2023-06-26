import time
def selection_sort(arr):
    start = time.time()
    n = len(arr)
    
    for i in range(n-1):
        # Assume the current element is the minimum
        min_index = i
        
        # Find the minimum element in the remaining unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end = time.time()
    time_taken = end-start
    print("Total time taken to execute: ",time_taken)
# Example usage:
arr = [5, 3, 8, 4, 2]
selection_sort(arr)
print(arr)
