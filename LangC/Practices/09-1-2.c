#include <stdio.h>

double CelToFah (double num)
{
	return 1.8*num + 32;
}
double FahToCel (double num)
{
	return (num-32)/1.8;
}

int main (void)
{
	int num;
	double degree;
	printf("어떤 온도를 입력하겠습니까?\n");
	printf("1.섭씨(Celsius) 2.화씨(Fahrenheit): ");
	scanf("%d", &num);

	switch(num)
	{
	case 1:
		printf("온도를 입력하세요: ");
		scanf("%lf", &degree);
		printf("입력한 온도는 화씨로 %f도입니다.\n", CelToFah(degree));
		break;
	case 2:
		printf("온도를 입력하세요: ");
		scanf("%lf", &degree);
		printf("입력한 온도는 섭씨로 %f도입니다.\n", FahToCel(degree));
		break;
	default:
		printf("다른 옵션은 없습니다. 처음부터 다시 시작하세요.\n");
	}

	return 0;
}
