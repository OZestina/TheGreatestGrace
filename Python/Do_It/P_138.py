a = [(1,2),(3,4),(5,6)]
for i in a:
    print(i)

for (i,j) in a:
    print(i+j)

a = range(10)
print(a)    #range(0,10), 0~9 정수 10개

add=0
for i in range(1,100):
    add += i
print(add)

#리스트 내포, list comprehension
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

result2 = [num*3 for num in a if num%2==0]
print(result2)

result3 = [x*y for x in range(2,10)
           for y in range(1,10)]
print(result3)
