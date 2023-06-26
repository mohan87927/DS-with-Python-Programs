
#Program for Stack

def push(s,limit):
    if len(s)<limit:
        elm=input("Enter a elelment to push to the stack: ")
        s.append(elm)
        print("The Updated stack:")
        print(s)
    else:
        print("stack is full")
        print("Remove elements to add elements.....!")

def pop(s):
    if len(s)!=0:
        print("The Element ",s.pop(-1),"popped form the stack")
        print("The Updated Stack:")
        print(s)
    else:
        print("Stack has no elements to pop")

def traverse(s):
    if len(s)!=0:
        for i in s:
            print(i)
    else:
        print("Stack has no Elements to Traverse")

def limit(s):
    limit = int(input("Enter the limit for the Stack: "))
    
    

def Stack():
    s=[]
    limit=int(input("Enter the limit for the stack: "))
    
    while True:
        
        print("1. Push")
        print("2. Pop")
        print("3. traverse")
        print("0. Exit")
        
        opt=input("Enter a Option to Continue: ")

        if opt == "1":
            push(s,limit)

        elif opt == "2":
            pop(s)

        elif opt == "3":
            traverse(s)

        elif opt == "0":
            break

        else:
            print("Enter a Valid option....!")

#Program for Queue

def enqueue(q,limit):
    if len(q)<limit:
        elm=input("Enter a Element to add to the Queue: ")
        q.append(elm)
        print("Updated Queue: ")
        print(q)
    else:
        print("Queue is full")
        print("Remove elements to add elements to the queue")

def dequeue(q):
    if len(q)!=0:
        print("The element ",q.pop(0),"Removed form the Queue")
        print("Updated Queue: ")
        print(q)
    else:
        print("The Queue has no elements to Remove")

def traverse(q):
    if len(q)!=0:
        for i in q:
            print(i)
    else:
        print("The Queue has no ellements to traverse")

def Queue():
    
    q=[]
    limit=int(input("Enter the limit of the Queue: "))

    while True:

        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Traverse")
        print("0. Exit")

        opt = input("Enter a option to Continue: ")

        if opt == "1":
            enqueue(q,limit)

        elif opt == "2":
            dequeue(q)

        elif opt == "3":
            traverse(q)

        elif opt == "0":
            break

        else:
            print("Enter a valid option....!")

#Main program 

while True:
    print("")
    print("1. Stack")
    print("2. Queue")
    print("0. Exit")
    print("")
    opt = input("Enter a option to continue: ")

    if opt == "1":
        Stack()

    elif opt == "2":
        Queue()

    elif opt == "0":
        print("Progam ended......:)")
        break

    else:
        print("Enter a Valid option.....!")

