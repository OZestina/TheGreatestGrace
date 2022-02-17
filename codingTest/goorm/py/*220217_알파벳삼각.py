# https://level.goorm.io/exam/49070/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EC%82%BC%EA%B0%81-%EC%9E%A5%EB%82%9C%EA%B0%90/quiz/1

# 1st try
# 최댓값이 다르다..?

height = int(input())
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

result = [0] * height
result[0] = alphabet[input()]

for _ in range(height-1):
	temp = input()
	
	result[0] = result[0] + alphabet[temp[0]]
	result[len(temp)-1] = result[len(temp)-2] + alphabet[temp[len(temp)-1]]
	
	for i in range(1, len(temp)-1):
		a = result[i] + alphabet[temp[i-1]]
		b = result[i] + alphabet[temp[i]]
		result[i] = a if a < b else b

print(max(result))
