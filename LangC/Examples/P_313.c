//ArrayParamAccess.c

#include <stdio.h>

void ShowArayElem(int*param, int len)
{
	int i;
	for (i=0; i<len; i++)
		printf("%d ", param[i]);
	printf("\n");
}

void AddArayElem(int*param, int len, int add)
{
	int i;
	for(i=0; i<len; i++)
		param[i] += add;
}

int main(void)
{
	int arr1[3] = {1,2,3};
	AddArayElem(arr1, sizeof(arr1)/sizeof(int), 1);
	ShowArayElem(arr1, sizeof(arr1)/sizeof(int));
	
	AddArayElem(arr1, sizeof(arr1)/sizeof(int), 2);
	ShowArayElem(arr1, sizeof(arr1)/sizeof(int));

	AddArayElem(arr1, sizeof(arr1)/sizeof(int), 3);
	ShowArayElem(arr1, sizeof(arr1)/sizeof(int));
	return 0;
}
