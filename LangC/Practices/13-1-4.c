#include <stdio.h>

int main(void)
{
	int arr[6] = {1,2,3,4,5,6};
	int *first=&arr[0], *last=&arr[5];
	int i, temp;

	for(i=0; i<3; i++)
	{
		temp = *first;
		*first = *last;
		*last = temp;
		first++; last--;
	}

	for(i=0; i<6; i++)
		printf("%d ", arr[i]);

	return 0;
}
