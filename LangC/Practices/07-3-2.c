//1st try -> 왜 안되는 지 모르겠음... -> 알아냄! (line 10의 while문에서 나갈 수 있는 방법이 없어서 그랬음!)

#include <stdio.h>

int main(void)
{
	int sum=0, i=0;
	while(i<101)
	{
		while(i%2 == 0)
			sum += i;
		
		//printf("%d", i); //제대로 도는 지 확인용 -> 안돌아감
		i++;
	}
	
	printf("0이상 100이하의 정수 중 짝수의 합은 %d입니다.\n", sum);
	return 0;
}

//2nd try -> 돌아가긴 함 벋뜨! (to be continued on 3rd try)
#include <stdio.h>

int main(void)
{
	int sum=0, i=0;
	while(i<101)
	{
		while(i%2 == 0)
		{
			sum += i;
			i++;
		}
		i++;
	}
	
	printf("0이상 100이하의 정수 중 짝수의 합은 %d입니다.\n", sum);
	return 0;
}

//3rd try (답지^^;;)
//'짝수'만 더하는 거니까 굳이 홀수를 거칠 필요가 없었던 것이다..! (깨달음)

#include <stdio.h>

int main(void)
{
	int sum=0, i=0;

	do
	{
		sum += i;
		i += 2;
	}while(i <101);

	printf("0이상 100이하의 정수 중 짝수의 합은 %d입니다.\n", sum);
	return 0;
}
