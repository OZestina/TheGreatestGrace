//1st way
//변수를 char로 선언. 디버깅 에러 발생
//숫자를 입력받아 저장하는데 char 변수에 저장하려고 해서 안된것.
//char는 128진법을 쓰는 아이라고 생각하자^^ㅎㅎ

#include <stdio.h>

int main(void)
{
	char num1;
	printf("아스키 코드 값을 입력하세요: ");
	scanf("%d", &num1);
	printf("입력한 아스키 코드에 해당하는 문자는 %c입니다.\n", num1);

	return 0;
}


//답지 보고 int로 바꾸니 에러 없음. 왜지? -> 이제 앎!

#include <stdio.h>

int main(void)
{
	int num1;
	printf("아스키 코드 값을 입력하세요: ");
	scanf("%d", &num1);
	printf("입력한 아스키 코드에 해당하는 문자는 %c입니다.\n", num1);

	return 0;
}
