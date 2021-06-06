//EmployeeManager1.cpp
//main function


int main(void)
{
	//직원 관리를 목적으로 설계된 컨트롤 클래스의 객체 생성
	EmployeeHandler handler;

	//직원 등록
	handler.AddEmployee(new PermanentWorker("Kim", 5000));
	handler.AddEmployee(new PermanentWorker("Lee", 1500));
	handler.AddEmployee(new PermanentWorker("Jun", 2000));

	//이번 달에 지불해야 할 급여의 정보
	handler.ShowAllSalaryInfo();

	//이번 달에 지불해야 할 급여의 총합
	handler.ShowTotalSalary();

	return 0;
}
