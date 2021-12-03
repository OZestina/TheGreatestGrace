#https://level.goorm.io/exam/49101/%ED%99%98%EA%B2%BD%EA%B3%BC-%EC%A5%90-%ED%81%AC%EA%B8%B0%EC%9D%98-%EC%83%81%EA%B4%80%EA%B4%80%EA%B3%84/quiz/1

#3rd try
#딕셔너리보다 배열로하는게 메모리 더 적게쓰고 더 빠름ㅎ (머쓱)
def goodOrBad(array):
	# 주어진 배열의 최솟값-2 이상 최댓값+2 이하에 대응할 수 있도록 배열 생성
	# (사실상 의미가 없는 최솟값-2, 최댓값+2 등이 포함된건 for문 내의 코드를 심플하기 하기 위한 것)
	values = [0] * (max(array)- min(array) + 5)
	#배열 인덱스와 실제 크기를 계산하기 위한 고정수를 미리 저장해둠
	posDifference = min(array)-2
	
	# 배열로 주어진 수를 1회 반복하면서 각 수가 카운트되는 크기(-2 ~ +2)의 배열자리에 +1 해줌
	for i in array:
		values[i-posDifference] += 1
		values[i-posDifference+1] += 1
		values[i-posDifference+2] += 1
		values[i-posDifference-1] += 1
		values[i-posDifference-2] += 1
	#가장 큰 value를 갖는 배열의 인덱스 + 고정수를 리턴	
	return values.index(max(values)) + posDifference

input()
clean = [int(x) for x in input().split(" ")]
dirty = [int(x) for x in input().split(" ")]

cleanResult = goodOrBad(clean)
dirtyResult = goodOrBad(dirty)
print(cleanResult, dirtyResult)
if cleanResult > dirtyResult: print("good")
else: print("bad")

#==========================================================
	
#1st try
#딕셔너리로 해봄
def goodOrBad(array):
	dic = dict()
	for i in range(min(array)-2, max(array)+3):
		dic[i] = 0

	for i in array:
		dic[i] += 1
		dic[i+1] += 1
		dic[i+2] += 1
		dic[i-1] += 1
		dic[i-2] += 1

	maximum = 0
	key = 0
	for i in dic.keys():
		if dic[i] > maximum:
			key = i
			maximum = dic[i]
	return key

input()
clean = [int(x) for x in input().split(" ")]
dirty = [int(x) for x in input().split(" ")]

cleanResult = goodOrBad(clean)
dirtyResult = goodOrBad(dirty)
print(cleanResult, dirtyResult)
if cleanResult > dirtyResult: print("good")
else: print("bad")

	
#2nd try
#딕셔너리 선언 및 max value값 찾기를 한줄로!
def goodOrBad(array):
	dic = {i:0 for i in range(min(array)-2, max(array)+3)}

	for i in array:
		dic[i] += 1
		dic[i+1] += 1
		dic[i+2] += 1
		dic[i-1] += 1
		dic[i-2] += 1

	key = max(dic, key=dic.get)
			
	return key

input()
clean = [int(x) for x in input().split(" ")]
dirty = [int(x) for x in input().split(" ")]

cleanResult = goodOrBad(clean)
dirtyResult = goodOrBad(dirty)
print(cleanResult, dirtyResult)
if cleanResult > dirtyResult: print("good")
else: print("bad")
