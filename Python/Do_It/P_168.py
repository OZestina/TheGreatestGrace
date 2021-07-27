number = input("input number: ")    #input은 무조건 str으로 받는다
print(number)
print(type(number))

print("a""b""c" "d")    #아무것도 안써도 됨!
print("a"+"c"+"e")      #사이에 +써도 됨!
print("A","B","c")      #근데 사이에 ',' 찍으면 띄어쓰기!!

f = open("new.txt", 'w')    #파일객체 = open(파일명, 파일모드) #r읽기, w쓰기(덮어쓰기), a추가
for i in range(1,11):
    data = "%d line\n" % i
    f.write(data)
f.close()
