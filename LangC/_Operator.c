//연산자(Operator)

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

