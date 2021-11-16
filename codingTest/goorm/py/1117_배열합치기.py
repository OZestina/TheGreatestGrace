#https://level.goorm.io/exam/43250/%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0/quiz/1

def listPrint(array):
	for i in array:
		print(i, end=" ")
		
user_input_1 = input()
arrayA = [int(x) for x in input().split(" ")]
arrayB = list(map(int, input().split(" ")))

arraySum = arrayA + arrayB
arraySum.sort()

listPrint(arraySum)
