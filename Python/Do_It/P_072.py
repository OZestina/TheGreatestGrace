# 빈 리스트
a = []
b = list()

b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, ['life', 'is']]

x = 'a' + '2'
y = 'a'+str(2)
print(x)
print(y)

print(b)
print(b[0]+b[2])    #4
print(b[-3])        #1
print(b[-len(b)])   #1

print(e[2])
print(e[2][0])
print(d[1:2])   #2 #[n:m] n이상 m미만
print(d[:2])    #[1,2]
print(d[3:])    #['is']
print(d[3])     #is

print(b+c)  #list 합치기
print(b*3)  #list 반복하기
c[2] = 'very'
print(c)    #['life', 'is', 'very', 'short']
del c[2]
print(c)    #['life', 'is', 'short']
del e[2:]
print(e)    #[1, 2]
