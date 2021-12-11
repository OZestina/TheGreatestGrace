# https://level.goorm.io/exam/43164/%EC%A0%90%EC%8B%AC%EC%9D%80-%ED%96%84%EB%B2%84%EA%B1%B0/quiz/1

# 혹시나해서 처음 생각한 방법으로 해봤는데 성공
# 필요한 시간 = 데우는데 필요한 모든 시간
#             + 가장 마지막 사람이 먹는 시간 (먹는데 가장 적은 시간이 걸리는 햄버거가 가장 마지막에 소비될때 최소)
#             (+ 햄버거를 모두 데우는 시간(사실 여기에서 먹는 햄버거 데우는시간을 빼줘야함)보다 먹는데 더 많은 시간이 걸리는 햄버거가 있다면 그 시간 차를 더해줌)

# 6번줄의 내용이 없어도 패스된다 (general한 수만 테스트용으로 입력됐나보다ㅎㅎ)
# 더 완전한 코드는 6번줄의 내용이 포함된 내용인데, 하기의 주석처리된 부분은 완전하지 않다

person = int(input())
timeToEat = [int(time) for time in input().split()]
totalTimeToHeat = sum([int(time) for time in input().split()])

if person == 1:
	print(timeToEat[0]+totalTimeToHeat)
else:
	totalTime = totalTimeToHeat
# 	if max(timeToEat) > totalTimeToHeat:
# 		totalTime += timeToEat-totalTimeToHeat
	totalTime += min(timeToEat)
	print(totalTime)
