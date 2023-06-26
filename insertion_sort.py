def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_array(arr):
    print("Sorted array:")
    for num in arr:
        print(num, end=" ")
    print()

def get_user_array():
    arr = []
    size = int(input("Enter the size of the array: "))
    for i in range(size):
        num = int(input(f"Enter element {i + 1}: "))
        arr.append(num)
    return arr

def menu():
    print("Insertion Sort Program")
    print("-----------------------")
    print("1. Sort array")
    print("2. Exit")

arr = []
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        arr = get_user_array()
        insertion_sort(arr)
        print_array(arr)
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the program!")
