//Car.h

#ifndef __CAR_H__
#define __CAR_H__

namespace CAR_CONST
{
	enum
	{
		ID_LEN	=20,
		MAX_SPD	=200,
		FUEL_STEP	=2,
		ACC_STEP	=10,
		BRK_STEP	=10
	};
}


class Car
{
private:
	char gamerID[CAR_CONST::ID_LEN];
	int fuelGauge;
	int curSpeed;
public:
	void InitMembers(char*ID, int fuel);
	void ShowCarState();	//상태정보 출력
	void Accel();			//엑셀, 속도증가
	void Break();			//브레이크, 속도감소
};

#endif
