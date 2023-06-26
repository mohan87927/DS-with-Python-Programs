def factorial(num):
    if num<0:
        print("Enter a valid number")
        return
    elif num==0:
        return 1
    else:
        return num*factorial(num-1)


num=int(input("ENter a number"))
f=factorial(num)
print(f)
