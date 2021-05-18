#include <stdio.h>

int main(void)
{
	FILE * info = fopen("mystory.txt", "at");

	if(info ==NULL)
	{
		puts("File open failed");
		return -1;
	}

	fputs("#즐겨먹는 음식: 짬뽕, 탕수육\n", info);
	fputs("#취미: 야구관람\n", info);

	fclose(info);
	return 0;
}
