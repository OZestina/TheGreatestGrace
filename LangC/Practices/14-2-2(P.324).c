//line8 에서 ptr에 저장된 ㄱ밧을 const로 선언되지 않은 포인터 변수에 대입하고 있다.
//(내 컴퓨터 바탕으로) 컴파일 되기는 하지만 (num값이 20으로 변경), const 선언을 무의미하게 만드는 문장의 삽입이어서 잘못

#include <stdio.h>

void SD(const int * ptr)
{
	int * rptr = ptr;
	printf("%d\n", *rptr);
	*rptr = 20;
}
int main(void)
{
	int num = 10;
	int * ptr = &num;
	SD(ptr);
	printf("%d\n", num);
	return 0;
}
