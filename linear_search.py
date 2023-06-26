import time
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not found

def insert_element():
    elm=int(input("Enter element to Insert: "))
    arr.append(elm)

def display():
    print("Elements of array are: ")
    for i in arr:
        print(i)

arr=[]
 
while True:
    
    print("")
    print("1. Insert Element")
    print("2. Display Elements")
    print("3. Search")
    print("0. Exit")
    print("")

    choice = input("Enter an option to continue: ")

    if choice == "1":
        insert_element()

    elif choice == "2":
        display()

    elif choice == "3":
        target=int(input("Enter element to search: "))
        start=time.time()
        index = linear_search(arr, target)
        end=time.time()
        if index != -1:
            print(f"Element {target} found at index {index}")
        else:
            print("Element not found")
        print("Time taken to search is ",end-start)

    elif choice == "0":
        print("Program Ended...")
        break

    else:
        print("Enter a valid option")    
