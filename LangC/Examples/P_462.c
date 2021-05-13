//InitStructArray.c

#include <stdio.h>

struct person
{
	char name[20];
	char phoneNum[20];
	int age;
};

int main(void)
{
	struct person arr[3] = {
		{"A", "001", 21},
		{"B", "002", 37},
		{"C", "003", 19}
	};

	int i;
	for(i=0; i<3; i++)
	{
		printf("%s %s %d \n", arr[i].name, arr[i].phoneNum, arr[i].age);
	}
	return 0;
}
