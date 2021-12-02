# https://level.goorm.io/exam/49096/%EC%96%B4%EB%B6%80%EC%9D%98-%EA%B3%A0%EA%B8%B0%EC%9E%A1%EC%9D%B4/quiz/1

[length,fishes] = [int(x) for x in input().split()]
fishmap = [int(x) for x in input().split()]

count = 0
for i in range(length):
	fish = 0
	for j in range(i, length):
		fish += fishmap[j]
		if fish == fishes:
			count += 1
		elif fish > fishes:
			break
			
print(count)
