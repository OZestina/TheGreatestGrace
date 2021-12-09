# https://level.goorm.io/exam/43219/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%92%A4%EC%A7%91%EA%B8%B0/quiz/1

#1st try
#역순으로 반복되는 iterator를 reversed()로 생성해 하나씩 프린트
user_input = input()
for i in reversed(user_input):
	print(i, end='')
  
#2nd try
#reversed()로 생성한 iterator를 join해 string으로 만들고 프린트
user_input = input()
result = "".join(reversed(user_input))
print(result)
