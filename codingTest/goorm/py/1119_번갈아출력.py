#https://level.goorm.io/exam/43110/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B2%88%EA%B0%88%EC%95%84-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
word = input()
length = len(word)

newWord = ""
for i in range(length//2):
	newWord += word[i]+word[length-1-i]
if length % 2:
	newWord += word[(length)//2]
	
print(newWord)
