#include <stdio.h>

int main(void)
{
	int arr[5] = {1,2,3,4,5};
	int *ptr = &arr[4];
	int i, sum=0;

	for(i=5; i>0; i--)
	{
		sum += *ptr;  //11~12의 두 줄은 sum += *(ptr--); 로 합칠 수 있다!
		ptr--;
	}

	printf("%d\n", sum);

	return 0;
}
