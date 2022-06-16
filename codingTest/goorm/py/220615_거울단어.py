# https://level.goorm.io/exam/49066/%EA%B1%B0%EC%9A%B8-%EB%8B%A8%EC%96%B4/quiz/1

mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p', 's':'z', 'z':'s', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'u':'u', 'v':'v', 'w':'w', 'x':'x'}

user_input = int(input())
for i in range(user_input):
	temp = input()
	for j in range(int((len(temp)+1) / 2)):
		if temp[j] not in mirror:
			print("Normal")
			break
		elif mirror[temp[j]] != temp[len(temp)-1 - j]:
			print("Normal")
			break
	else:
		print("Mirror")
