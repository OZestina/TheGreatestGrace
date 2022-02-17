# https://level.goorm.io/exam/49080/%EC%88%AB%EC%9E%90-%EB%B8%94%EB%9F%AD-%EC%8C%93%EA%B8%B0/quiz/1

# 1st try
# 10번 Timeout 뜸 => sort 없이 진행하는 방법을 생각해보자
user_input = int(input())
count = 0
current_num = 0
queue = []
for _ in range(user_input * 2):
	order = input()
	if order == 'remove':
		current_num += 1
		if queue[len(queue)-1] != current_num:
			count += 1
			queue.sort(reverse=True)
		queue.pop()
	else:
		queue.append(int(order[4:]))

print(count)


# 2nd try (220217)
# 6 Fail (런타임도 아니고 실패?)
user_input = int(input())
count = 0	#정렬 횟수 카운트
current_num = 0	#이번에 remove할 수
queue = []	#add된 숫자
falseCount = 0	#정렬된 queue에 append된 횟수

for _ in range(user_input * 2):
	order = input()
	if order == 'remove':
		current_num += 1
		if falseCount != 0:	#정렬된 상태가 아니면
			position = len(queue)-1
			while queue[position] < current_num:
				position -= 1
			if queue[position] != current_num:
				count += 1
				falseCount = 0
	else:
		queue.append(int(order[4:]))
		falseCount += 1
print(count)
