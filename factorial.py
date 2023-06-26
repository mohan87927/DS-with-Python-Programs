def factorial(num):
    if num <0:
        return "Enter a valid number"
    elif num ==0 :#or num==1:
        return 1
    else:
        return num*factorial(num-1) 

while True:
    num=int(input("Enter  a number: "))
    print(factorial(num))
