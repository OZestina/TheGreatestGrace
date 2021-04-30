//연산자(Operator)

/*
0. sizeof 연산자
//변수, 상수 및 "자료형의 이름"을 피연산자로 연산 가능하다!
*/
#include <stdio.h>
int main()
{
	char ch = 9;
	int inum = 1052;
	double dnum = 3.1415;
	printf("변수 ch의 크기: %d \n", sizeof(ch));
	printf("변수 inum의 크기: %d \n", sizeof(inum));
	printf("변수 dnum의 크기: %d \n", sizeof(dnum));

	printf("char의 크기: %d \n", sizeof(char));
	printf("int의 크기: %d \n", sizeof(int));
	printf("long의 크기: %d \n", sizeof(long));
	printf("long long의 크기: %d \n", sizeof(long long));
	printf("float의 크기: %d \n", sizeof(float));
	printf("double의 크기: %d \n", sizeof(double));
	return 0;
}

/*
1. 복합 대입 연산자
a=a+b 를 간단히-> a+=b
a=a-b 를 간단히-> a-=b
a=a*b 를 간단히-> a*=b
a=a/b 를 간단히-> a/=b
a=a%b 를 간단히-> a%=b
*/

/*
2. 증가&감소 연산자
++i (선 증가, 후 연산)
--i (선 감소, 후 연산)
i++ (선 연산, 후 증가)
i-- (선 연산, 후 감소)
*/

//num1: 9, num2: 12 출력
//(int num2 선언에서) 소괄호로 묶여있더라도 "다음 문장으로 넘어가야만" 값의 증가/감소가 이뤄진다
#include <stdio.h>
int main(void)
{
	int num1 = 10;
	int num2 = (num1--)+2;

	printf("num1: %d \n", num1);
	printf("num2: %d \n", num2);
	return 0;
}

/*
3. 관계 연산자 (비교 연산자)
// <, >, ==, !=, <=, >=
관계 연산자들은 조건을 만족하면 1(참, true)을, 만족하지 않으면 0(거짓, false)을 반환한다.
*/

#include <stdio.h>
int main(void)
{
	int num1=10;
	int num2=12;
	int result1, result2, result3;

	result1=(num1==num2);
	result2=(num1<=num2);
	result3=(num1>num2);

	printf("result1: %d\n", result1);
	printf("result2: %d\n", result2);
	printf("result3: %d\n", result3);
	return 0;
}

/*
4. 논리 연산자
&& (AND) - 2개씩인거 ㄱ하자!
|| (OR) - 2개씩인거 ㄱ하자!
! (NOT) - 익숙하지 않은 개념... ㄱ합시당!
*/

#include <stdio.h>
int main(void)
{
	int num1=0; //0은 거짓을 의미
	int num2=1; //1은 참을 의미 (0이 아닌 수는 참으로 인식)
	int result1, result2;

	result1=(!num1); //거짓이 아님 -> 참(1)
	result2=(!num2); //참이 아님 -> 거짓(0)

	printf("result1: %d\n", result1); //1
	printf("result2: %d\n", result2); //0
	return 0;
}

/*
5. 비트 연산자
& (비트단위 AND) // 1&1만 1로 반환
| (비트단위 OR)
^ (비트단위 XOR) // 두 개의 비트가 서로 다른 경우에 1을 반환
~ (보수연산, 피연산자의 모든 비트를 반전시킨다) // ~num : num은 변화 없이 반전 결과만 반환
<< (피연산자의 비트열을 왼쪽으로 이동) // num<< : num은 변화 없이 두 칸 왼쪽 이동 결과만 반환 // 1칸 왼쪽 이동 시마다 두 배가 됨!
>> (피연산자의 비트열을 오른쪽으로 이동) // num>> : num은 변화 없이 두 칸 오른쪽 이동 결과만 반환 // 1칸 오른쪽 이동 시마다 2로 나눠짐!
*/

// & (비트단위 AND)
#include <stdio.h>
int main(void)
{
	int num1 = 15;		// 00001111
	int num2 = 20;		// 00010100
	int num3 = num1 & num2;	// 00000100 (4)
	printf("AND 연산의 결과: %d \n", num3);
	return 0;
}

// | (비트단위 OR)
#include <stdio.h>
int main(void)
{
	int num1 = 15;		// 00001111
	int num2 = 20;		// 00010100
	int num3 = num1 | num2;	// 00011111 (31)
	printf("OR 연산의 결과: %d \n", num3);
	return 0;
}

// ^ (비트단위 XOR)
#include <stdio.h>
int main(void)
{
	int num1 = 15;		// 00001111
	int num2 = 20;		// 00010100
	int num3 = num1 ^ num2;	// 00011011 (27)
	printf("XOR 연산의 결과: %d \n", num3);
	return 0;
}

// ~ (비트단위 보수연산)
#include <stdio.h>
int main(void)
{
	int num1 = 15;			// 00001111 (15)
	int num2 = ~num1;		// 11110000 (-16)
	int num3 = ~num2;		// 00001111 (15)
	printf("NOT 연산의 결과: %d %d \n", num2, num3);
	return 0;
}

// << (피연산자의 비트열을 왼쪽으로 이동)
#include <stdio.h>
int main(void)
{
	int num1 = 15;		// 00001111 (15)
	int result1 = num1<<1;	// 00011110 (30)
	int result2 = num1<<2;	// 00111100 (60)
	int result3 = num1<<3;	// 01111000 (120)

	printf("1칸 왼쪽 이동 결과: %d \n", result1);
	printf("2칸 왼쪽 이동 결과: %d \n", result2);
	printf("3칸 왼쪽 이동 결과: %d \n", result3);
	return 0;
}

// 음수일 경우도 같음!
#include <stdio.h>
int main(void)
{
	int num1 = -15;		// 11110001 (-15)
	int result1 = num1<<1;	// 11100010 (-30)
	int result2 = num1<<2;	// 11000100 (-60)
	int result3 = num1<<3;	// 10001000 (-120)

	printf("1칸 왼쪽 이동 결과: %d \n", result1);
	printf("2칸 왼쪽 이동 결과: %d \n", result2);
	printf("3칸 왼쪽 이동 결과: %d \n", result3);
	return 0;
}

// >> (피연산자의 비트열을 오른쪽으로 이동)
#include <stdio.h>
int main(void)
{
	int num1 = 48;		// 00110000 (48)
	int result1 = num1>>1;	// 00011000 (24)
	int result2 = num1>>2;	// 00001100 (12)
	int result3 = num1>>3;	// 00000110 (6)

	printf("1칸 오른쪽 이동 결과: %d \n", result1);
	printf("2칸 오른쪽 이동 결과: %d \n", result2);
	printf("3칸 오른쪽 이동 결과: %d \n", result3);
	return 0;
}

// 음의 경우에는, CPU에 따라 값이 달라질 수 있다
// 내 컴퓨터는 왼쪽에 생긴 빈 칸을 1로 채워서 음의 값을 유지하면서 절반 값으로 연산된다!
#include <stdio.h>
int main(void)
{
	int num1 = -48;		// 00110000 (-48)
	int result1 = num1>>1;	// 00011000 (-24)
	int result2 = num1>>2;	// 00001100 (-12)
	int result3 = num1>>3;	// 00000110 (-6)

	printf("1칸 오른쪽 이동 결과: %d \n", result1);
	printf("2칸 오른쪽 이동 결과: %d \n", result2);
	printf("3칸 오른쪽 이동 결과: %d \n", result3);
	return 0;
}

/*
6.포인터 연산자
> &: 피연산자(변수)의 주소값을 반환하는 반환하는 연산자 (&num) //상수는 &연산의 피연산자가 될 수 없다
> *: 포인터가 가리키는 메모리 공간에 접근할 때 사용하는 연산자

포인터 변수 초기화 시 0이나 NULL을 사용해 메모리 공간에 영향을 미치지 않도록 널 포인터를 이용해 초기화해둘 수 있다. (하기 둘 다 work)
int * ptr1 = 0;
int * ptr2 = NULL; 
*/

