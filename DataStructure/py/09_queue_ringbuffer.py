#Ringbuffer(링버퍼)를 이용해
#오래된 데이터를 버리는 (가장 최근 n개만 저장하는) 자료구조 구현

n = int(input('저장할 정수 개수 입력: '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input(f'{cnt+1}번째 정수 입력: '))
    cnt += 1

    retry = input('계속할까요? (Y...Yes, N...NO): ')
    if retry in ['N', 'n']:
        break

#출력을 시작하는 i번째 값의 i를 구하는 방법 
i = cnt - n
#입력한 수가 배열의 길이보다 적으면 인덱스는 0부터
if i < 0 : i = 0

while i < cnt:  #n만큼 돌아보자
    #i+1번째 값은 i%n에 들어있다
    print(f'{i + 1}번째: {a[i % n]}')
    i += 1
