#include <iostream>
using namespace std;

class Calculator
{
private:
	int T_Add;
	int T_Min;
	int T_Mul;
	int T_Div;

public:
	void Init();
	double Add(double n1, double n2);
	double Min(double n1, double n2);
	double Div(double n1, double n2);
	double Mul(double n1, double n2);
	void ShowOpCount();
};

void Calculator::Init()
{
	T_Add = 0;
	T_Min = 0;
	T_Mul = 0;
	T_Div = 0;
}

double Calculator::Add(double n1, double n2)
{
	T_Add++;
	return n1+n2;
}

double Calculator::Min(double n1, double n2)
{
	T_Min++;
	return n1-n2;
}

double Calculator::Div(double n1, double n2)
{
	T_Div++;
	return n1/n2;
}

double Calculator::Mul(double n1, double n2)
{
	T_Mul++;
	return n1*n2;
}

void Calculator::ShowOpCount()
{
	cout<<"덧셈: "<<T_Add<<" ";
	cout<<"뺄셈: "<<T_Min<<" ";
	cout<<"곱셈: "<<T_Mul<<" ";
	cout<<"나눗셈: "<<T_Div<<endl;
}

int main(void)
{
	Calculator cal;
	cal.Init();
	cout<<"3.2 + 2.4 = "<<cal.Add(3.2, 2.4)<<endl;
	cout<<"3.5 / 1.7 = "<<cal.Div(3.5, 1.7)<<endl;
	cout<<"2.2 - 1.5 = "<<cal.Min(2.2, 1.5)<<endl;
	cout<<"4.9 + 1.2 = "<<cal.Div(4.9, 1.2)<<endl;
	cal.ShowOpCount();

	return 0;
}
