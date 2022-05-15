# https://level.goorm.io/exam/43056/%EA%B0%80%EC%9C%84%EB%B0%94%EC%9C%84%EB%B3%B4/quiz/1

r = s = p = 0
user_input = input().split()
for choice in user_input:
	if choice == '1': s += 1
	elif choice == '2': r += 1
	else: p += 1
	
if r == 5 or s == 5 or p == 5: print(0)
elif r > 0 and s > 0 and p > 0: print(0)
else:
	if r == 0: print(s)
	else: print(p) if s == 0 else print(r)
