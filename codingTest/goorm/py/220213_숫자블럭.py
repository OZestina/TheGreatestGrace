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


# 2nd try
# 아 왜 
user_input = int(input())
count = 0
current_num = 0
queue = []
sort = False
for _ in range(user_input * 2):
	order = input()
	if order == 'remove':
		current_num += 1
		if sort == True:
			pass
		elif queue[len(queue)-1] != current_num:
			count += 1
			sort = True
		# queue.remove(current_num)
	else:
		queue.append(int(order[4:]))
		sort = False

print(count)
