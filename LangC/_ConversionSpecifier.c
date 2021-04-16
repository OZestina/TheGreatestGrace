//Conversion Specifier, 서식문자 (출력의 형태를 지정하는 용도)

//%d (int, char, short) 10진수 정수 형태 출력 & 입력
//%ld (long) 10진수 정수 형태 입력
//%lld (long long) 10진수 정수 형태 입력

//하기의 예제를 컴파일하면 9/2의 몫=4 로 나오는데, 이는 4.5의 정수 (4)만을 출력하는 것 (%d가 10진수의 정수를 출력하는 서식문자여서 소숫점 생략됨!)
#include <stdio.h>
int main(void)
{
	int num1 = 9, num2=2;
	printf("%d/%d의 몫=%d \n" , num1, num2, num1/num2);
	return 0;
}

//%u (unsigned int) 부호 없는 10진수 정수 출력

//%o, %#o (unsigned int) 부호 없는 8진수 정수 출력 & 입력
//%x, %X, %#x, %#X (unsigned int) 부호 없는 16진수 정수 출력 & 입력

//%f (float, double) 10진수 실수 형태 출력
	// (float) 10진수 실수 형태 입력

//%lf (double) 10진수 실수 형태 입력

//%Lf (long double) 10진수 실수 형태 출력
	// (long double) 10진수 실수 형태 입력

//%e, %E (float, double) e 또는 E 방식의 10진수 실수 형태 출력
	// (float) 10진수 실수 형태 입력

//%g, %G (float, double) 값에 따라 %f와 %e (%E) 사이에서 출력 형태 선택 //보통 소숫점이 7자리 이상이면  %e 방식으로 출력
	// (float) 10진수 실수 형태 입력

//%c (char, int, short) 값에 대응하는 문자 입출력 (ASCII 코드 문자)

//%s (char*) 문자열의 출력 & 입력(배열)

//%p (void*) 포인터의 주소 값
