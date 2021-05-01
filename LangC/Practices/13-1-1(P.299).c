#include <stdio.h>

int main(void)
{
	int arr[5] = {1,2,3,4,5};
	int *ptr=arr;
	int i=0;

	for(; i<5; i++)
		*(ptr+i) += 2;
	
	for(i=0; i<5; i++)
		printf("%d ", arr[i]);
	return 0;
}


//출제자가 원한 방식^^;; (ptr의 값을 바꾸는 것)

#include <stdio.h>

int main(void)
{
	int arr[5] = {1,2,3,4,5};
	int *ptr=arr;
	int i=0;

	for(; i<5; i++)
	{
		*ptr += 2;
		ptr++;
	}
	
	for(i=0; i<5; i++)
		printf("%d ", arr[i]);
	return 0;
}
