
stack=[]

def Push():
    item=int(input("Enter an item to Add to the Stack: "))
    stack.append(item)
    print("The updated Stack is: ")
    print(stack)

def Pop():
    if len(stack)==0:
        print("The Stack is empty")
    else:
        print("The popped item from stack is ",stack.pop(-1))

def Display():
    if len(stack)==0:
        print("Stack has no elements to display")
    else:
        print("The Items of Stack are: ")
        for i in stack:
            print(i)

while True:
    print("")
    print("1. Push Item")
    print("2. Pop Item")
    print("3. Display Items of Staack")
    print("0. Quit")
    print("")
    
    Operation = int(input("Enter a Number to continue: "))
    print("")

    if Operation==1:
        Push()

    elif Operation==2:
        Pop()

    elif Operation==3:
        Display()

    elif Operation==0:
        print("Program Ended")
        break

    else:
        print("Enter a Valid Option")
    
    
