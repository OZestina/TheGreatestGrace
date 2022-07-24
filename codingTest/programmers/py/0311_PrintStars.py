# https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3

#1st try
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a)
    
#2nd
#for 반복문 안쓰고, 바로 print로 쓸 수 있는 방법!
#/n 어떻게 사용하는 지 잊어버려서 처음부터 이렇게 못한건 안비밀ㅠㅠ

a, b = map(int, input().strip().split(' '))
print(('*' * a + '\n') * b)
