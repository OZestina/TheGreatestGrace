#include <stdio.h>

int main(void)
{
	int num1=10, num2=20;
	int* ptr1=&num1, *ptr2=&num2;

	(*ptr1) += 10;
	(*ptr2) -= 10;

	ptr1=&num2;
	ptr2=&num1;

	printf("%d, %d\n", *ptr1, *ptr2);

	return 0;
}

// 출제자가 원한건 이거였을듯... (추가적인 포인터 변수를 이용한 ptr1, ptr2의 변환)

#include <stdio.h>

int main(void)
{
	int num1=10, num2=20;
	int* ptr1=&num1, *ptr2=&num2;
	int* temp;

	(*ptr1) += 10;
	(*ptr2) -= 10;

	temp=ptr1;
	ptr1=ptr2;
	ptr2=temp;

	printf("%d, %d\n", *ptr1, *ptr2);

	return 0;
}
