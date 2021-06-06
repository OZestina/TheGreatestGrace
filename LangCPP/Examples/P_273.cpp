//EmployeeManager1.cpp

#include <iostream>
#include <cstring>
using namespace std;

class PermanentWorker
{
private:
	char name[100];
	int salary;
public:
	PermanentWorker (char * name, int money): salary(money)
	{
		strcpy(this->name, name);
	}
	int GetPay() const
	{
		return salary;
	}
	void ShowSalaryInfo() const
	{
		cout<<"Name: "<<name<<endl;
		cout<<"Salary: "<<salary<<endl<<endl;
	}
};
