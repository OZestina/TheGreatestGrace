# 빅데이터분석_2일차
# https://cafe.daum.net/bigmega/pJVC/5907

hobby = []
for i in range(3):
    data = input("your hobby? ")
    hobby.append(data)

print(hobby)
print('# of hobby: '+str(len(hobby)))

for i in hobby:
    print(i, end = ' ')


menu = input("먹고싶은 음식은? ")
if menu =="자장면":
    print("중국집으로 가요")
elif menu == "회":
    print("일식집으로 가요")
elif menu == "떡볶이":
    print("분식집으로 가요")
else:
    print("집에서먹어요")

price = 5000
cup = 3
total = price*cup
if total > 10000:
    total -= 2000
print("지불할 금액은 "+str(total)+"원입니다.")

food = []
for i in range(3):
    data = input("food리스트에 추가>> ")
    food.append(data)
print(food[1])
print(food[:2])
print(food[1:])
food[0] = "라면"
print(food)

month = 10
if 3<= month<=5:
    season = "봄"
elif 6<= month <=8:

    season = "여름"
elif 9 <= month <= 11:
    season = "가을"
elif month==12 | 1<=month<=2 :
    season = "겨울"
print("지금 계절은 "+season+"입니다")

sum = 0
for i in range(10,21):
    sum += i
print(sum)

target = 55
times = 0
while True:
    data = input("숫자를 입력하세요>> ")
    times += 1
    if int(data) == target:
        break
    elif int(data) >55:
        print("더 작은 수를 입력하세요")
    else:
        print("더 큰 수를 입력하세요")
print("축하합니다. "+str(times)+"번 만에 맞췄어요")

start = int(input('시작값을 입력하세요>> '))
end = int(input('끝값을 입력하세요>> '))
count = end - start +1
sum = 0
for i in range(start, end+1):
    sum+= i
print('개수는 '+str(count)+'개, 합은 '+str(sum)+'입니다')

rank = ['김연아','나몰라','김상화','모태범']
del rank[1]
rank[2] = '모모범'
for i in range(len(rank)):
    print(str(i+1)+'위 '+rank[i])
