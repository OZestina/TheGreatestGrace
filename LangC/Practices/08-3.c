//ㅋㅋㅋㅋㅋ 내 답. 모든 경우의 수 적기
#include <stdio.h>

int main(void)
{
	int n;
	printf("정수 입력: ");
	scanf("%d", &n);

	switch(n)
	{
	case 0:
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:
	case 6:
	case 7:
	case 8:
	case 9:
		printf("0이상 10 미만\n");
		break;
	case 10:
	case 11:
	case 12:
	case 13:
	case 14:
	case 15:
	case 16:
	case 17:
	case 18:
	case 19:
		printf("10이상 20 미만\n");
		break;
	case 20:
	case 21:
	case 22:
	case 23:
	case 24:
	case 25:
	case 26:
	case 27:
	case 28:
	case 29:
		printf("20이상 30 미만\n");
		break;
	default:
		printf("30이상\n");
	}

	return 0;
}


//답지. 더 똑똑하다^^

#include <stdio.h>

int main(void)
{
	int n;
	printf("정수 입력: ");
	scanf("%d", &n);

	switch(n/10)
	{
	case 0:
		printf("0이상 10 미만\n");
		break;
	case 1:
		printf("10이상 20 미만\n");
		break;
	case 2:
		printf("20이상 30 미만\n");
		break;
	default:
		printf("30이상\n");
	}
	return 0;
}
