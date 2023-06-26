import time
def reversed_string(string,rev_str):
    stack=[]
    for i in string:
        stack.append(i)
    for j in range(len(stack)):
        rev_str += stack.pop(-1)
    return rev_str

rev=""
string=input("Enter a string: ")
start_time=time.time()
rev=reversed_string(string,rev)
end_time=time.time()
print("Time taken: ",end_time-start_time)
print("reversed string: ",rev)
