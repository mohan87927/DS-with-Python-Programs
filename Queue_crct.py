import time
queue=[]

def enqueue():
        elm=input("Enter a Element to add to the Queue: ")
        queue.append(elm)
        print("Updated Queue: ")
        print(queue)

def dequeue():
    if len(queue)!=0:
        print("The element ",queue.pop(0),"Removed form the Queue")
        print("Updated Queue: ")
        print(queue)
    else:
        print("The Queue has no elements to Remove")

def Display():
    if len(queue)!=0:
        for i in queue:
            print(i)
    else:
        print("The Queue has no ellements to traverse")

while True:

    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("0. Exit")

    opt = input("Enter a option to Continue: ")

    if opt == "1":
        enqueue()

    elif opt == "2":
        dequeue()

    elif opt == "3":
        start=time.time()
        Display()
        end=time.time()
        print("TIme taken:",end-start,"seconds")

    elif opt == "0":
        print("Program Ended")
        break

    else:
        print("Enter a valid option....!")

