#include <stdio.h>

int main(void)
{
	int i=0, num, sum;
	double result=0.0;

	printf("몇 개의 정수를 입력하겠습니까?: ");
	scanf("%d", &num);

	while(i <num)
	{
		printf("%d번째 정수를 입력하세요: ",i+1);
		scanf("%d", &sum);
		result += sum;
		i++;
	}
	printf("입력한 정수의 평균값은 %f입니다\n", result/num);
	return 0;
}
