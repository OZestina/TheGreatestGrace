#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int WhereBlank(char str[])
{
	int i;
	for (i=0; i<strlen(str); i++)
		if(str[i]==' ')
			return i;
	return -1;
}

int SameName(char str1[], char str2[])
{
	int x1=WhereBlank(str1);
	int x2=WhereBlank(str2);

	if(x1 != x2)
		return 0;
	else
		return !strncmp(str1, str2, x1);
}

int SameAge(char str1[], char str2[])
{
	int x1=WhereBlank(str1);
	int x2=WhereBlank(str2);
	int age1, age2;

	age1 = atoi(&str1[x1+1]);
	age2 = atoi(&str2[x2+1]);

	if(age1==age2)
		return 1;
	else
		return 0;
}

int main(void)
{
	char str1[20];
	char str2[20];

	printf("첫 번째 사용자의 정보를 입력하세요.(이름 나이)");
	fgets(str1, sizeof(str1),stdin);
	
	printf("두 번째 사용자의 정보를 입력하세요.(이름 나이)");
	fgets(str2, sizeof(str2),stdin);

	if(SameName(str1,str2))
		puts("이름이 동일합니다.");
	else
		puts("이름이 동일하지 않습니다.");

	if(SameAge(str1,str2))
		puts("나이가 같습니다.");
	else
		puts("나이가 같지 않습니다.");

	return 0;
}
