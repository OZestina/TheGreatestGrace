#include <iostream>

int main(void)
{
	double rate = 0.12;
	int num, salary;

	while(1)
	{
		std::cout<<"판매 금액을 만원 단위로 입력(-1 to end): ";
		std::cin>>num;
		if(num==-1)
		{
			std::cout<<"프로그램을 종료합니다.\n";
			break;
		}
		salary = 50+(num*0.12);
		std::cout<<"이번달 급여: "<<salary<<"만원\n";
	}
	
	return 0;
}

//답지 보고 리코드!
// 1) 급여 계산 함수화 2) 변수 이름 문맥에 맞게

#include <iostream>

int CalSalary(int sales)
{
	return (int)(50 + sales * 0.12);
}

int main(void)
{
	int sales;

	while(1)
	{
		std::cout<<"판매 금액을 만원 단위로 입력(-1 to end): ";
		std::cin>>sales;
		if(sales==-1)
		{
			std::cout<<"프로그램을 종료합니다.\n";
			break;
		}
		std::cout<<"이번달 급여: "<<CalSalary(sales)<<"만원\n";
	}
	
	return 0;
}
