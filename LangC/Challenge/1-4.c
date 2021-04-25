#include <stdio.h>

void Func(int num)
{
	int i, j, k;

	for (i=1; i<7; i++)
		for (j=1; j<5; j++)
			for (k=1; k<8; k++)
				if ((500*i+700*j+400*k) == num)
					printf("크림빵 %d개, 새우깡 %d개, 콜 라 %d개\n", i, j, k);	
}

int main(void)
{
	printf("현재 당신이 소유하고 있는 금액: 3,500원\n");
	Func(3500);
	printf("어떻게 구입하시겠습니까?\n");

	return 0;
}
