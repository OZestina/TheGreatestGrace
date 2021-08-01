f = open('new.txt', 'w')
for i in range (1,11):
    data = "line no. %d입니다\n" % i
    f.write(data)
f.close()

f1 = open('new.txt', 'r')
while True:
    line = f1.readline()
    if not line:
        break
    print(line)
f1.close()

f2 = open('new.txt', 'r')
lines = f2.readlines()
for line in lines:
    print(line)
f2.close()

f3 = open('new.txt', 'r')
data2 = f3.read()
print(data2)
f3.close()

f4 = open('new.txt', 'a')
for i in range (11,21):
    data = "line no. %d입니다\n" % i
    f4.write(data)
f4.close()

# with open() as f: 로 파일을 열면,
# with 블록을 벗어나는 순간 열린 객체 f가 자동으로 close된다
with open('new.txt', 'w') as f5:
    for i in range(21, 31):
        data = "line no. %d입니다\n" % i
        f5.write(data)



#명령 프롬프트에서 파일명 + 인자 전달
# import sys
# args = sys.argv[1:]     # sys모듈의 argv는 명령창에서 입력한 인수를 의미.
#                         # 첫 번째 인수가 파일명이므로 그를 제외한 뒤따라오는 인수가 args에 저장됨
# for i in args:
#     print(i)

