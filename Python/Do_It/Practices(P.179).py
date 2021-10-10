#Q1
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False

is_even = lambda x : True if x%2==0 else False

#Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result+=i
    return result/len(args)

#Q3
input1 = input("enter 1st number")
input2 = input("enter 2nd number")
total = int(input1) + int(input2)
print("sum of two numbers is %s" %total)

#Q5
with open("test.txt", "w") as f:
    f.write("Life is too short")
with open("test.txt", "r") as f1:
    print(f1.read())

#Q6
user_input = input("write what you want to keep>> ")
with open("test.txt","a") as f:
    f.write(user_input)
    f.write('\n')
with open("test.txt","r") as f:
    print(f.read())

#Q7
with open('test.txt', 'r') as f:
    body = f.read()
body = body.replace("java","python")
with open('test.txt', 'a') as f:
    f.write(body)
with open('test.txt', 'r') as f:
    print(f.read())
