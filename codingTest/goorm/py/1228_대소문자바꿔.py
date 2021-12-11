# https://level.goorm.io/exam/43090/%EB%8C%80%EC%86%8C%EB%AC%B8%EC%9E%90-%EB%B0%94%EA%BE%B8%EC%96%B4-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/quiz/1

def changeAlphabet(word):
	newWord = ''
	small = 'abcdefghijklmnopqrstuvwxyz'
	big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in word:
		if letter in small:
			newWord += big[small.find(letter)]
		elif letter in big:
			newWord += small[big.find(letter)]
		else:
			newWord += letter
	return newWord

user_input = input()
print(changeAlphabet(user_input))
