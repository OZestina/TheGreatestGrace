//답지보고 레고!: 피보나치 수열 n개를 프린트하는 함수 작성 (함수 안의 printf만 사용해서, 반환값은 void!)
#include <stdio.h>
void Fibonacci (int);

int main(void)
{
	int num;
	printf("출력할 피보나치 수열의 길이를 입력하세요: ");
	scanf("%d", &num);

	if (num<1)
	{
		printf("1 이상의 수를 입력하세요.\n");
		return -1;
	}
	
	Fibonacci(num);
	return 0;
}

void Fibonacci(int num)
{
	int f1=0, f2=1, f3, i;
	if(num==1)
		printf("%d", f1);
	else
		printf("%d %d ", f1, f2);

	for (i=0; i<num-2; i++)
	{
		f3 = f1+f2;
		printf("%d ",f3);
		f1=f2;
		f2=f3;
	}
}


//내가 푼거: 피보나치 수열 n번째를 구하는 함수 작성 (재귀함수)
//재귀함수 각인줄 알았는데, 다른 방법이 더 연산 적게하는 방법이었다...
#include <stdio.h>
int Fibonacci (int);

int main(void)
{
	int i, num;
	printf("출력할 피보나치 수열의 길이를 입력하세요: ");
	scanf("%d", &num);

	if (num<1)
	{
		printf("1 이상의 수를 입력하세요.\n");
		return -1;
	}
	
	for (i=0; i <num; i++)
		printf("%d, ", Fibonacci(i+1));
	printf("...\n");

	return 0;
}

int Fibonacci(int num)
{
	if(num==1)
		return 0;
  else if(num==2)
		return 1;
	else
		return Fibonacci(num-1)+Fibonacci(num-2);
}
