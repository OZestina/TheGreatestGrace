# https://level.goorm.io/exam/43241/%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1

[n1, oper, n2] = input().split()
if oper == '+':
	print(int(n1)+int(n2))
elif oper == '-':
	print(int(n1)-int(n2))
elif oper == '*':
	print(int(n1)*int(n2))
elif oper == '/':
	result = str(int(n1)/int(n2)) + '0'
	print(result[:5])
