import time

def hash_function(key):
    return key % 60

print("1. Generate hash values")
print("2. Exit")

records = []
while True:
    opt = int(input("Enter a choice: "))
    if opt == 1:
        reg_no = input("Register No: ")
        name = input("Name: ")
        phn = input("Enter your phone number: ")
        email = input("Enter your email id: ")
        address = input("Enter your address: ")

        l = [reg_no, name, phn, email, address]
        records.append(l)

        start_time = time.time()
        key = 0
        for i in reg_no:
            if reg_no.isdigit():
                key += int(i)
            else:
                key += ord(i)
        key += records.index(l)
        end_time = time.time()

        print("Time taken:", end_time - start_time)
        print("Hash value is:", hash_function(key))

    elif opt == 2:
        print("Program ended")
        break
    else:
        print("Enter a valid choice...!")
