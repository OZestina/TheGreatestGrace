#include <iostream>

void swap (int * n, int * m)
{
	int temp = *n;
	*n = *m;
	*m = temp;
}

void swap (char* c, char* d)
{
	char n = *c;
	*c = *d;
	*d = n;
}

void swap (double *n, double * m)
{
	double temp = *n;
	*n = *m;
	*m = temp;
}

int main(void)
{
	int num1=20, num2=30;
	swap(&num1, &num2);
	std::cout<<num1<<' '<<num2<<std::endl;

	char ch1 = 'A', ch2 = 'Z';
	swap(&ch1, &ch2);
	std::cout<<ch1<<' '<<ch2<<std::endl;

	double d1=1.111, d2=5.555;
	swap(&d1, &d2);
	std::cout<<d1<<' '<<d2<<std::endl;

	return 0;
}
