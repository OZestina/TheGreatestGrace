//숙제 중 1)배열로 만들기 3)문제 3->4개로 만들기 진행 완료 (2021.04.11 밤)
//2)함수로 만들기 진행중.....

#include <stdlib.h>  //rand함수 사용을 위해 필요!
#include <stdio.h>
#include <time.h>

int main()
{
	int nums[4];
	int getnums[4];
	int strike=0, ball=0, outt=0;
	int num = 0;
	
	srand(time(NULL));
	nums[0] = rand() % 9 + 1;
	nums[1] = rand() % 9 + 1;
	nums[2] = rand() % 9 + 1;
	nums[3] = rand() % 9 + 1;

	while (nums[0] == nums[1]) {
		nums[1] = rand() % 9 + 1;
	}

	while (nums[0] == nums[2] || nums[1] == nums[2]) {
		nums[2] = rand() % 9 + 1;
	}

	while (nums[0] == nums[3] || nums[1] == nums[3] || nums[2] == nums[3] ) {
		nums[3] = rand() % 9 + 1;
	}

	/*printf("%d %d %d \n", nums[0], nums[1], nums[2]);*/ 

	while (strike != 4) {

		if (num == 0) {
			printf("(야구게임) 1~9 사이의 중복되지 않는 숫자의 수열을 맞춰보세요\n%d번째 시도입니다. \n", num+1);
		}
		else {
			printf("%d 스트라이크, %d 볼, %d 아웃, 다시 시도해보세요.\n%d번째 시도입니다. \n", strike, ball, outt, num);
		}

		scanf_s("%d %d %d %d", &getnums[0], &getnums[1], &getnums[2], &getnums[3]);
		num++;

		strike = 0, ball = 0, outt = 0;

		//getnums[0]
		if (getnums[0] == nums[0])
			strike++;
		else if (getnums[0] == nums[1] || getnums[0] == nums[2] || getnums[0] == nums[3])
			ball++;
		else
			outt++;
		//getnums[1]
		if (getnums[1] == nums[1])
			strike++;
		else if (getnums[1] == nums[0] || getnums[1] == nums[2]|| getnums[1] == nums[3])
			ball++;
		else
			outt++;
		//getnums[2]
		if (getnums[2] == nums[2])
			strike++;
		else if (getnums[2] == nums[1] || getnums[2] == nums[0]|| getnums[2] == nums[3])
			ball++;
		else
			outt++;
		//getnums[3]
		if (getnums[3] == nums[3])
			strike++;
		else if (getnums[3] == nums[1] || getnums[3] == nums[0]|| getnums[3] == nums[2])
			ball++;
		else
			outt++;

	}
		
	if (strike == 4)
		printf("4 스트라이크! 축하합니다. \n%d번 만에 성공했어요.\n", num);
	
	
	
	return 0;
}
