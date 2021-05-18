//허허허... 서식문자 주의합시다! (입력이랑 출력이 다른 경우도 있음!)

#include <stdio.h>
#define PI		3.1415
#define AREA(x)	((x)*(x)*PI)

int main(void)
{
	double num1;
	printf("Enter radius: ");
	scanf("%lf", &num1);

	printf("%g를 반지름으로 하는 원의 넓이: %g", num1, AREA(num1));
	
	return 0;
}
