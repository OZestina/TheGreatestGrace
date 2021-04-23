//답지를 보고 BigNum과 SmallNu만 다시!
//아래처럼 return에 조건 연산자로 진행 시 num1 vs num2를 한 번만 비교해도 된다! (꺌뀸)

int BigNum(int num1, int num2, int num3)
{
	if (num1>=num2)
		return (num1>=num3)? num1: num3;
	else
		return (num2>=num3)? num2: num3;
}
int SmallNum(int num1, int num2, int num3)
{
	if (num1<=num2)
		return (num1<=num3)? num1: num3;
	else
		return (num2<=num3)? num2: num3;

//1st try
#include <stdio.h>
int ReadNum(void);
int BigNum(int, int, int);
int SmallNum(int, int, int);
void HowToUse(void);

int main(void)
{
	int num1, num2, num3;
	
	HowToUse();

	num1 = ReadNum();
	num2 = ReadNum();
	num3 = ReadNum();

	printf("%d, %d, %d 중 가장 큰 수는 %d입니다.\n", num1, num2, num3, BigNum(num1, num2, num3));
	printf("%d, %d, %d 중 가장 작은 수는 %d입니다.\n", num1, num2, num3, SmallNum(num1, num2, num3));

	return 0;
}

int ReadNum(void)
{
	int num;
	scanf("%d", &num);
	return num;
}
int BigNum(int num1, int num2, int num3)
{
	if (num1>=num2 && num1>=num3)
		return num1;
	else if (num2>num1 && num2>=num3)
		return num2;
	else
		return num3;
}
int SmallNum(int num1, int num2, int num3)
{
	if (num1<=num2 && num1<=num3)
		return num1;
	else if (num2<num1 && num2<=num3)
		return num2;
	else
		return num3;
}
void HowToUse(void)
{
	printf("이 프로그램은 여러분이 입력한 세 가지 수 중 \"가장 큰 수\"와 \"가장 작은 수\"를 출력합니다.\n");
	printf("같은 수의 경우, 먼저 입력된 수가 출력돼요.\n");
	printf("이제 세개의 수를 입력해주세요.\n");
}
