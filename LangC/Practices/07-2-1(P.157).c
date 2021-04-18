#include <stdio.h>

int main(void)
{
	int i=0, num, sum=0;
	
	printf("5개의 정수를 입력하세요.\n");
	
	while (i<5)
	{
		printf("%d번째 정수: ", i+1);
		scanf("%d", &num);
		while (num < 1)
		{
			printf("1보다 큰 수를 입력하세요.");
			scanf("%d", &num);
		}

		i++;
		sum += num;
	}
	printf("입력한 5개 정수의 합은 %d입니다.\n", sum);
	return 0;
}
