a = True
b = False
c = 1

print(type(a))  #<class 'bool'>
print(type(b))  #<class 'bool'>
print(type(c))  #<class 'int'>

print(1==c)     #True

d = [1,2,3,4]

print(bool('a'))    #True
print(bool(""))     #False
print(bool(0))      #False
print(bool(-1))     #True
print(bool(d))      #True

while d:
    print(d.pop())

print(bool(d))      #False (빈 것은 False)
