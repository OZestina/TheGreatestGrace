#include <stdio.h>

int main(void)
{
	FILE * info = fopen("mystory.txt", "rt");
	char str[20];
	
	if(info ==NULL)
	{
		puts("File open failed");
		return -1;
	}

	while(fgets(str, sizeof(str), info)!=NULL)
		printf(str);


	fclose(info);
	return 0;
}
