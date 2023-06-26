brackets=[]
dup=[]
rev=[]
while True:
    print("Enter n to stop appending brackets.....!")
    b = input("Enter Brackets: ")
    if b.lower() != "n":
        brackets.append(b)
    else:
        break
dup=brackets
while len(dup)!=0:
    rev.append(dup.pop())


for j in rev:
    print(j)
