//StructValAddress.c

#include <stdio.h>

struct point
{
	int xpos;
	int ypos;
};

struct person
{
	char name[20];
	char phoneNum[20];
	int age;
};

int main(void)
{
	struct point pos = {10, 20};
	struct person man = {"Ken", "010-3564-2356", 37};

	printf("%p %p \n", &pos, &pos.xpos);
	printf("%p %p %p\n", &man, man.name, &man.name[0]);
	return 0;
}
