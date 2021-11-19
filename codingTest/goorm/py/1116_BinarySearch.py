#https://level.goorm.io/exam/43064/binary-search/quiz/1

def findNum(arr, num):
	pl = 0
	pr = len(arr)-1
	pc = (pl+pr)//2
	while pl < pr:
		if arr[pc] == num:
			return pc+1
		elif arr[pc] < num:
			pl = pc+1
			pc = (pl+pr)//2
		else:
			pr = pc - 1
			pc = (pl+pr)//2
	return "X"

user_input = input()
# array = list(map(int, input().split(" ")))
array = [int(x) for x in input().split(" ")]
num = int(input())

print(findNum(array, num))



#2nd try
#제공되는 이진탐색함수 사용

import bisect

user_input = input()
array = [int(x) for x in input().split(" ")]
num = int(input())

pos = bisect.bisect(array,num)
if array[pos-1] == num: print(pos)
else: print('X')
