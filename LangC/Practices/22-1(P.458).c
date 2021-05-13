#include <stdio.h>

struct employee
{
	char name[20];
	char ID[20];
	int salary;
};

int main(void)
{
	struct employee man1;

	printf("이름 입력: ");
	scanf("%s", man1.name);
	printf("주민등록번호 입력: ");
	scanf("%s", man1.ID);
	printf("급여 정보 입력: ");
	scanf("%d", &(man1.salary));

	printf("이름: %s \n", man1.name);
	printf("주민등록번호: %s \n", man1.ID);
	printf("급여 정보: %d \n", man1.salary);

	return 0;
}
