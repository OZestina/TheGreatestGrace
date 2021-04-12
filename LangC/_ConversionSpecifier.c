//Conversion Specifier, 서식문자 (출력의 형태를 지정하는 용도)

//%d 10진수 정수 형태의 출력
//하기의 예제를 컴파일하면 9/2의 몫=4 로 나오는데, 이는 4.5의 정수 (4)만을 출력하는 것 (%d가 10진수의 정수를 출력하는 서식문자여서 소숫점 생략됨!)
#include <stdio.h>
int main(void)
{
	int num1 = 9, num2=2;
	printf("%d/%d의 몫=%d \n" , num1, num2, num1/num2);
	return 0;
}



