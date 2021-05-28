//RacingMain.cpp

//필요한 헤더와 함수를 Car.h와 Car.cpp에 다 넣으니까,
//실제 실행 파일인 아래 코드에서는 #include "Car.h"만 추가하면 되네!

#include "Car.h"

int main(void)
{
	Car run99;
	run99.InitMembers("run99", 100);
	run99.Accel();
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	return 0;
}
