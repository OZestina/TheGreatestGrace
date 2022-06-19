# https://level.goorm.io/exam/149359/%EA%B8%B0%EB%B3%B8-%EC%82%AC%ED%83%95-%EA%B0%80%EC%A0%B8%EA%B0%80%EA%B8%B0/quiz/1

user_input = input()

games = input().split()
groom = 0
friend = 0
for game in games:
	if int(game) % 2 == 0:
		friend += 1
	else:
		groom += 1
if friend > groom:
	print(friend)
elif groom > friend:
	print(groom)
else:
	print("tie")
