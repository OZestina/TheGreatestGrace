#include <stdio.h>

struct employee
{
	char name[20];
	char ID[20];
	int salary;
};

int main(void)
{
	struct employee arr[3];
	int i;

	for(i=0; i<3; i++)
	{
		printf("이름 입력: ");
		scanf("%s", arr[i].name);
		printf("주민등록번호 입력: ");
		scanf("%s", arr[i].ID);
		printf("급여 정보 입력: ");
		scanf("%d", &(arr[i].salary));
	}
	
	for(i=0; i<3; i++)
	{
		printf("%s %s %d \n", arr[i].name, arr[i].ID, arr[i].salary);
	}
	
	return 0;
}
