# https://level.goorm.io/exam/47878/%EC%82%AC%EC%9D%80%ED%92%88-%EA%B5%90%ED%99%98%ED%95%98%EA%B8%B0/quiz/1

user_input = int(input())

for i in range(user_input):
	[season, normal] = [int(i) for i in input().split()]
	t_season = season // 5
	t_normal = normal // 7
	if t_season <= t_normal:
		print(t_season)
	elif t_season == 0:
		print(0)
	else:
		temp = t_normal
		season -= 5 * t_normal
		normal -= 7 * t_normal
		if season + normal >= 12:
			temp += 1
			season -= 12 - normal
		if season >= 12:
			temp += season // 12
		print(temp)
