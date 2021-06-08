//EmployeeManager3.cpp

#include <iostream>
#include <cstring>
using namespace std;

class Employee
{
private:
	char name[100];
public:
	Employee(char * name)
	{
		strcpy(this->name, name);
	}
	void ShowYourName() const
	{
		cout<<"Name: "<<name<<endl;
	}
};

class PermanentWorker : public Employee
{
private:
	int salary;	//monthly pay
public:
	PermanentWorker(char * name, int money) : Employee(name), salary(money)
	{}
	int GetPay() const
	{
		return salary;
	}
	void ShowSalaryInfo() const
	{
		ShowYourName();
		cout<<"Salary: "<<GetPay()<<endl<<endl;
		// cout<<"Salary: "<<salary<<endl<<endl; //이것도 되는 지 확인해보기!
	}
};

class TemporaryWorker : public Employee
{
private:
	int workTime;
	int payPerHour;
public:
	TemporaryWorker(char * name, int pay): Employee(name), workTime(0), payPerHour(pay)
	{}
	void AddWorkHour(int time)
	{
		workTime += time;
	}
	int GetPay() const
	{
		return workTime*payPerHour;
	}
	void ShowSalaryInfo() const
	{
		ShowYourName();
		cout<<"Salary: "<<GetPay()<<endl<<endl;
	}
};

class SalesWorker : public PermanentWorker
{
private:
	int salesResult;
	double bonusRatio;
public:
	SalesWorker(char * name, int money, double ratio): PermanentWorker(name, money), bonusRatio(ratio)
	{}
	void AddSalesResult(int value)
	{
		salesResult += value;
	}
	int GetPay() const
	{
		return PermanentWorker::GetPay()+(int)(salesResult*bonusRatio);

	}
	void ShowSalaryInfo() const
	{
		ShowYourName();
		cout<<"Salary: "<<GetPay()<<endl<<endl;
	}
};

class EmployeeHandler
{
private:
	Employee* empList[50];
	int empNum;
public:
	EmployeeHandler(): empNum(0)
	{}
	void AddEmployee (Employee* emp)
	{
		empList[empNum++] = emp;
	}
	void ShowAllSalaryInfo() const
	{
		/*
		for(int i=0; i<empNum; i++)
			empList[i]->ShowSalaryInfo();
		*/
	}
	void ShowTotalSalary() const
	{
		int sum = 0;
		/*
		for(int i=0; i<empNum; i++)
			sum += empList[i]->GetPay();
		*/
		cout<<"Salary sum: "<<sum<<endl;
	}
	~EmployeeHandler()
	{
		for(int i=0; i<empNum; i++)
			delete empList[i];
	}
};

int main(void)
{
	//직원 관리를 목적으로 설계된 컨트롤 클래스의 객체 생성
	EmployeeHandler handler;

	//직원 등록_정규직
	handler.AddEmployee(new PermanentWorker("KIM", 1000));
	handler.AddEmployee(new PermanentWorker("Lee", 1500));

	//직원 등록_임시직
	TemporaryWorker * alba = new TemporaryWorker("Jung", 700);
	alba->AddWorkHour(5);
	handler.AddEmployee(alba);

	//직원 등록_sales
	SalesWorker * seller = new SalesWorker("Hong", 1000, 0.1);
	seller->AddSalesResult(7000);
	handler.AddEmployee(seller);

	//이번 달에 지불해야 할 급여의 정보
	handler.ShowAllSalaryInfo();

	//이번 달에 지불해야 할 급여의 총합
	handler.ShowTotalSalary();
	return 0;
}
