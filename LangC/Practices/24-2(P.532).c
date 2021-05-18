//답지와 달라보여서 놀랐으나, 사실 같은 내용이었다!

#include <stdio.h>

int CalByte(FILE * ptr)
{
	long i, k;
	i=ftell(ptr);

	fseek(ptr, 0, SEEK_END);
	k=ftell(ptr);

	fseek(ptr,i,SEEK_SET);

	return k;
}

int main(void)
{
	FILE * fp = fopen("text.txt", "rt");
	printf("%d \n", CalByte(fp));
	
	return 0;
}


//답지

#include <stdio.h>
#include <string.h>

long GetFileSize(FILE * fp);

int main(void)
{
	char str[100];
	FILE * fp = fopen("text.txt", "rt");
	fgets(str, 100, fp);
	fputs(str, stdout);
	printf("파일의 크기: %ld \n", GetFileSize(fp));
	fgets(str, 100, fp);
	fputs(str, stdout);
	printf("파일의 크기: %ld \n", GetFileSize(fp));
	fgets(str, 100, fp);
	fputs(str, stdout);
	printf("파일의 크기: %ld \n", GetFileSize(fp));
	fclose(fp);
	
	return 0;
}

long GetFileSize(FILE * fp)
{
	long fpos;
	long fsize;
	fpos=ftell(fp);

	fseek(fp, 0, SEEK_END);
	fsize = ftell(fp);
	fseek(fp, fpos, SEEK_SET);
	return fsize;
}
