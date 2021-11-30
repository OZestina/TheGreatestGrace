#https://level.goorm.io/exam/49101/%ED%99%98%EA%B2%BD%EA%B3%BC-%EC%A5%90-%ED%81%AC%EA%B8%B0%EC%9D%98-%EC%83%81%EA%B4%80%EA%B4%80%EA%B3%84/quiz/1

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
