//어려웠당

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	int maxlen, len, i;
	char* str;

	printf("How long would you write your string?");
	scanf("%d", &maxlen);
	getchar();	//to delete \n
	str = (char*)malloc(sizeof(char)*(maxlen+1));	//NULL문자 고려해서 +1

	printf("Enter the string: ");
	fgets(str, maxlen+1, stdin);
	str[strlen(str)-1]=0;	//\n문자의 삭제
	len=strlen(str);

	for(i=len; i>0; i--)
	{
		if(str[i]==' ')
		{
			printf("%s ", &str[i+1]);
			str[i]=0;
		}
	}
	printf("%s", &str[0]);
	free(str);
	return 0;
}
