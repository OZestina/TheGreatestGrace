//SeedRamdonNum.c
//씨드 값이 동일하면 같은 난수 생성


#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int seed, i;
	printf("씨드 값 입력: ");
	scanf("%d", &seed);
	srand(seed);	//사용자는 씨를 뿌렸다. 효과는 굉장했다!

	for(i=0; i<5; i++)
		printf("정수 출력: %d \n", rand());
	return 0;
}
