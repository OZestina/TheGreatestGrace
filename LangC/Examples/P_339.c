//TwoDimArraySize.c

#include <stdio.h>

int main(void)
{
	int arr[3][4];
	int arr2[7][9];
	printf("세로 3, 가로4: %d \n", sizeof(arr));
	printf("세로 7, 가로9: %d \n", sizeof(arr2));
	return 0;
}
