//방법1) 변수 num의 값을 적절히 초기화 -> 첫 번째 반복조건의 검사결과가 '참'이 되도록
#include <stdio.h>

int main(void)
{
	int total = 0, num = 1;

	while(num!=0)
	{
		printf("정수 입력(0 to quit): ");
		scanf("%d", &num);
		total += num;
	}
	printf("합계: %d \n", total);
	return 0;
}

//방법2) while문 진입 전에 사용자로부터 1회 값 입력 받기
#include <stdio.h>

int main(void)
{
	int total = 0, num;

	printf("정수 입력(0 to quit): ");
	scanf("%d", &num);
	total += num;

	while(num!=0)
	{
		printf("정수 입력(0 to quit): ");
		scanf("%d", &num);
		total += num;
	}
	printf("합계: %d \n", total);
	return 0;
}
