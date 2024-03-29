#https://level.goorm.io/exam/49076/1%EC%B0%A8%EC%9B%90-%EB%BF%8C%EC%9A%94%EB%BF%8C%EC%9A%94/quiz/1

#1st try
#알파벳의 좌표를 기억하는 배열을 별도로 만들어서 스트링 업데이트 시 처음부터 검수하지 않도록하자

[N,M] = [int(x) for x in input().split(" ")]
result = input()

#각 알파벳의 첫 시작 위치 저장
idx = [0]
#반복되는 알파벳의 가장 마지막 수 저장
pos = 1

while pos < len(result):
	#r_idx가 result 길이보다 작을때 반복
	if len(idx) == 0:
		idx.append(pos)
	#idx에 마지막으로 저장된 알파벳과 현재 알파벳이 같을 경우 r_idx+1
	while pos < len(result) and result[pos] == result[idx[len(idx)-1]]:
		pos += 1
		# print(pos)
	#반복된 알파벳의 개수가 M 이상이면 해당 부분 삭제
	if pos - idx[len(idx)-1] >= M:
		result = result.replace(result[idx[len(idx)-1]]*(pos - idx[len(idx)-1]),'',1)
		pos = idx[len(idx)-1]
		del idx[len(idx)-1]
	#반복된 알파벳의 개수가 M 미만이면 r_idx를 idx배열에 추가
	else:
		idx.append(pos)
		pos += 1

if len(idx) == 0: print("CLEAR!")
else: print(result)
	
	
#2nd try
#배열을 사용하지 않고, 스트링 삭제 후 처음부터 진행하는 방법

[N,M] = [int(x) for x in input().split(" ")]
result = input()

#반복되는 알파벳의 첫 시작 위치 저장
idx1 = 0
#반복되는 알파벳의 마지막 위치 +1 저장
idx2 = 1

while idx2 < len(result):
	#idx에 마지막으로 저장된 알파벳과 현재 알파벳이 같을 경우 idx2+1
	while idx2 < len(result) and result[idx2] == result[idx1]:
		idx2 += 1
	#반복된 알파벳의 개수가 M 이상이면 해당 부분 삭제
	if idx2 - idx1 >= M:
		result = result.replace(result[idx1]*(idx2 - idx1),'',1)
		idx1 = 0
		idx2 = 1
		# print(result)
		# print("if: ", idx)
	#반복된 알파벳의 개수가 M 미만이면 r_idx를 idx배열에 추가
	else:
		idx1 = idx2
		idx2 += 1
	
if len(result) == 0:
	print("CLEAR!")
else:
	print(result)
