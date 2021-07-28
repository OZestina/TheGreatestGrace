target = 77
while True:
    a = int(input("your answer>> "))
    if a == target:
        print("correct!")
        break
    elif a >target:
        print("too big")
    else:
        print("too small")

todo_list = []
todo_list.append('play')
todo_list.append('eat')
print(len(todo_list))
for x in range(0,3):
    todo_list.append('sleep')
print(len(todo_list))
for x in range(0,3):
    data = input("what do you wanna do>> ")
    todo_list.append(data)
print(todo_list)

food_list = []
while True:
    data = input("input what you want to eat (x to exit)>> ")
    if data == "x":
        print("system exit")
        break
    else:
        food_list.append(data)
print(len(food_list))

id = input("id? ")
pw = input("pw? ")
print("your id is "+id+ "your pw is "+pw)

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print("sum: "+str(num1+num2))
print("subtraction: "+str(num1-num2))
print("multiply: "+str(num1*num2))
print("quotient: "+str(num1//num2))
print("remainder: "+str(num1%num2))

num = int(input("enter number: "))
if num%2 ==0:
    print("even number")
else:
    print("odd number")

goal = 1000
bonus_rate = 0.2
sales = int(input("enter sales: "))
if sales >= goal:
    print("congratulations")
    print("you got "+str(int(bonus_rate*sales))+" more this month")
else:
    print("your salary is normal")

for i in range (2,51,2):
    print(i, end = " ")
count=0
for i in range(1,1001):
    if i %3 ==0:
        count += 1
print(count)

name, age, tel = input("your name, age, tel>> ").split(sep=' ')
print(name)
print(age)
print(tel)

import random
target = random.randint(0,100)
while True:
    think = int(input("guess a number>> "))
    if think == target:
        break
    else:
        if think >target: print("too big")
        if think < target: print("too small")

def call2(x=200,y=100):
    print(x+y)
call2(x=100)
call2(333)

lis = ['100','200','300']
int_map = map(int,lis)
print(type(int_map))
int_list = list(int_map)
print(int_list)
print(type(int_list[0]))

import random
print(random.randint(0,10))
print(random.randrange(0,10))
print(random.choice(['a','b','c']))

import random
total = list()
random.seed(100)
for i in range(0,100):  #100번 반복(100명)
    person1 = []
    for x in range(0,5):    #5번 반복(5과목)
        person1.append(random.randint(50,100))  #50~100점
    total.append(person1)
print(len(total))   #100
print(total)
print('-------------')
sum=0
for person in total:
    sum = sum+person[0] #첫번째 과목 합
print(sum/len(total))
file = open("new.txt",'w')
for person in total:
    file.write(str(person))
    file.write('\n')
file.close()

file2 = open("new.txt",'r')
# print(file2.readline())
row1 = file2.readline()
print(row1)
str1 = row1.split("'\n'")
print(str1)
for i in range(len(str1)):
    print(str1[i])
person2 = list(str1)
print(person2)
print(type(person2))
print(person2[0])
str2 = person2[0].split(']')
print(str2[0])
str3 = str2[0].split(',')
print(str3[0].split('[')[1], str3[1],str3[2])
