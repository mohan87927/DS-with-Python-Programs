import time
import matplotlib.pyplot as plt
import numpy as np
def bubble_sort(arr):
    begin = time.time()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end = time.time()
    time_taken=end-begin
    print("Total time taken to execute: ",time_taken)
    return arr
# Test the algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

elements = np.array([i*500 for i in range(1,5)])
plt.xlabel("list length")
plt.ylabel("time complexity")
times=list()
for i in range(1,5):
    start=time.time()
    a=np.random.randint(500,size=i*500)

    bubble_sort(a)
    end=time.time()
    times.append(end-start)
    print("time taken to sort",i*500,"elemets is",end-start,"seconds")
plt.plot(elements,times,label="selection sort")
plt.grid()
plt.legend()
plt.show()
