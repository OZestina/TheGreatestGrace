# 구구단 프로그램
# 입력받은 단의 구구단을 출력해보자
def GuGu(n):
    print('===['+n+'단]===')
    for i in range(9):
        print(str(n), 'x', str(i+1), '=', str(int(n)*(i+1)))

gugu = input("출력할 단을 입력하세요>> ")
GuGu(gugu)

#3과 5의 배수의 총 합 구하기
sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

#게시판페이징
def getTotalPage(m,n):
    totalPage = m//n
    if m % n != 0:
        totalPage += 1

#메모장만들기
import sys
option = sys.argv[1]
if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)

#탭to4공백
import sys
ori_file = sys.argv[1]
new_file = sys.argv[2]
f = open(ori_file, 'r')
content = f.read().replace('\t',' '*4)
f.close()
f2 = open(new_file,'w')
f2.write(content)
f2.close()

