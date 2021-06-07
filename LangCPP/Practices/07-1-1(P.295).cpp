#include <iostream>
using namespace std;

class Car
{
private:
	int gasolineGauge;
public:
	Car(int gas): gasolineGauge(gas)
	{}
	int GetGasGauge() const
	{
		return gasolineGauge;
	}
};

class HybridCar : public Car
{
private:
	int electricGauge;
public:
	HybridCar(int gas, int elec): Car(gas), electricGauge(elec)
	{}
	int GetElecGauge() const
	{
		return electricGauge;
	}
};

class HybridWaterCar : public HybridCar
{
private:
	int waterGauge;
public:
	HybridWaterCar(int gas, int elec, int water) : HybridCar(gas, elec), waterGauge(water)
	{}
	void ShowCurrentGauge() const
	{
		cout<<"잔여 가솔린: "<<GetGasGauge()<<endl;
		cout<<"잔여 전기량: "<<GetElecGauge()<<endl;
		cout<<"잔여 워터량: "<<waterGauge<<endl;
	}
};

int main(void)
{
	HybridWaterCar car1(1, 2, 3);
	car1.ShowCurrentGauge();

	return 0;
}
