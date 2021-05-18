//입력받지 않아도 되는 거였는데 받아버렸넹^^

#include <stdio.h>

int main(void)
{
	FILE * info = fopen("mystory.txt", "wt");
	char str[20];

	if(info ==NULL)
	{
		puts("File open failed");
		return -1;
	}

	printf("이름을 입력하세요: ");
	fputs("#이름: ", info);
	fgets(str, sizeof(str), stdin);
	fputs(str, info);

	printf("주민번호를 입력하세요: ");
	fputs("#주민번호: ", info);
	fgets(str, sizeof(str), stdin);
	fputs(str, info);

	printf("전화번호를 입력하세요: ");
	fputs("#전화번호: ", info);
	fgets(str, sizeof(str), stdin);
	fputs(str, info);

	fclose(info);
	return 0;
}
