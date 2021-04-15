//ConvDiv.c
// 연산결과의 자료형은 피연산자의 자료형과 일치하기 때문에, num1/num2는 0이 되고 그 값이 double형으로 (자동)형 변환되어 divResult에 저장된다

#include <stdio.h>

int main()
{
	int num1=3, num2=4;
	double divResult;
	divResult = num1/num2;
	printf("나눗셈 결과: %f\n", divResult);

	return 0;
}

// num1, num2 둘 중 하나의 자료형이라도 double이면 연산결과가 double로 나와서 0.75가 출력된다

#include <stdio.h>

int main()
{
	int num1=3;
	double num2=4;
	double divResult;
	divResult = num1/num2;
	printf("나눗셈 결과: %f\n", divResult);

	return 0;
}
