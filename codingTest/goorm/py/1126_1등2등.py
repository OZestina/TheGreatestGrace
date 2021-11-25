#https://level.goorm.io/exam/49072/1%EB%93%B1%EA%B3%BC-2%EB%93%B1/quiz/1

ranking = input()
newRank = ranking.replace("12"," ",1).replace("21"," ",1)
newRank2 = ranking.replace("21"," ",1).replace("12"," ",1)
if len(ranking) - len(newRank) == 2 or len(ranking) - len(newRank2) == 2:
	print("Yes")
else:
	print("No")
