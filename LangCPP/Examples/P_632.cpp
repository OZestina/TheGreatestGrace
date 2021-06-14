//PowerfulCasting.cpp

#include <iostream>
using namespace std;

class Car
{
private:
	int fuelGauge;
public:
	Car(int fuel): fuelGauge(fuel) { }
	void ShowCarState() { cout<<"Remaining fuel: "<<fuelGauge<<endl; }
};

class Truck: public Car
{
private:
	int freightWeight;
public:
	Truck(int fuel, int weight): Car(fuel), freightWeight(weight) { }
	void ShowTruckState()
	{
		ShowCarState();
		cout<<"Weight of freight: "<<freightWeight<<endl;
	}
};

int main()
{
	Car * pcar1 = new Truck(80, 200);
	Truck * ptruck1 = (Truck*)pcar1;
	ptruck1->ShowTruckState();
	cout<<endl;

	Car * pcar2 = new Car(120);
	Truck * ptruck2 = (Truck*)pcar2;
	ptruck2->ShowTruckState();
	return 0;
}
