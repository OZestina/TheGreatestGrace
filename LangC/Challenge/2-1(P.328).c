#include <stdio.h>

void OddNum(int * ptr, int len)
{
	int i;

	printf("홀수 출력: ");
	for (i=0; i<len; i++)
		if (*(ptr+i) % 2 ==1)
			printf("%d ", *(ptr+i));
	printf("\n");
}
void EvenNum(int*ptr, int len)
{
	int i;

	printf("짝수 출력: ");
	for (i=0; i<len; i++)
		if (*(ptr+i) % 2 ==0)
			printf("%d ", *(ptr+i));
	printf("\n");
}

int main(void)
{
	int arr[10];
	int i;

	for(i=0; i<10; i++)
	{
		printf("정수 입력 (%d번째): ", i+1);
		scanf("%d", &arr[i]);
	}

	OddNum(arr, sizeof(arr)/sizeof(int));
	EvenNum(arr, sizeof(arr)/sizeof(int));
	return 0;
}
