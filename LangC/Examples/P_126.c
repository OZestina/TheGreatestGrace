//AutoConvOne.c

#include <stdio.h>

int main()
{
	double num1=245;
	int num2=3.1415;
	int num3=129;
	char ch=num3;
	double div;

	printf("정수 245를 실수로: %f \n", num1);
	printf("실수 3.1415를 정수로: %d \n", num2);
	printf("큰 정수 129를 작은 정수로: %d \n", ch);
	
	div = num3/num2;
	printf("int 변수의 나눗셈을 저장하는 변수만 double로 해서 진행할 수 있을까 (정수 실수): %d %f\n",div, div); //안됨
	return 0;
}
