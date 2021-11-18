#https://level.goorm.io/exam/49076/1%EC%B0%A8%EC%9B%90-%EB%BF%8C%EC%9A%94%EB%BF%8C%EC%9A%94/quiz/1

#1st try: 안됨
#알파벳의 좌표를 기억하는 

[N,M] = [int(x) for x in input().split(" ")]
result = input()

#각 알파벳의 첫 시작 위치 저장
idx = [0]
#반복되는 알파벳의 가장 마지막 수 저장
r_idx = 1

while r_idx < len(result):
	#r_idx가 result 길이보다 작을때 반복
	if len(idx) == 0:
		idx.append(r_idx)
	#idx에 마지막으로 저장된 알파벳과 현재 알파벳이 같을 경우 r_idx+1
	while r_idx < len(result) and result[r_idx] == result[len(idx)-1]:
		r_idx += 1
	#반복된 알파벳의 개수가 M 이상이면 해당 부분 삭제
	if r_idx - idx[len(idx)-1] >= M:
		result = result.replace(result[len(idx)-1]*(r_idx - idx[len(idx)-1]),'',1)
		r_idx = idx[len(idx)-1]
		del idx[len(idx)-1]
		# print(result)
		# print("if: ", idx)
	#반복된 알파벳의 개수가 M 미만이면 r_idx를 idx배열에 추가
	else:
		idx.append(r_idx)
		r_idx += 1
		# print("else: ", idx)
if len(idx) == 0:
	print("CLEAR!")
else:
	print(result)
