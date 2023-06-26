import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

# Get user input for the array
input_string = input("Enter the elements of the array (space-separated): ")
array = input_string.split()
converted_array = []
for num in array:
    converted_array.append(int(num))
array = converted_array

start = time.time()
sorted_array = insertion_sort(array)
end = time.time()

print("Sorted array:", sorted_array)
print("Time taken to sort is", end - start, "seconds")
