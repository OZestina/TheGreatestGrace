#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	int i, j, k=0;
	int w=0, e=0;
	char* a[3] = {"바위", "가위", "보"};
	char* b[3] = {"이겼습니다", "비겼습니다", "당신이 졌습니다"};

	srand((int)time(NULL));
	
	while(k!=2)
	{
		printf("바위는 1, 가위는 2, 보는 3: ");
		scanf("%d", &i);
		
		j=rand()%3;

		if(i-1==j){
			k=1; e++;}
		else if((i-1==0 && j==1)||(i-1==1 && j==2)||(i-1==2 && j==0)){
			k=0; w++;}
		else
			k=2;

		printf("당신은 %s 선택, 컴퓨터는 %s 선택, %s!\n", a[i-1], a[j], b[k]);
	}
	
	printf("게임의 결과: %d승, %d무\n", w, e);
	return 0;
}
