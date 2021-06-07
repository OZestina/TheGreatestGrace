//HASInheritance.cpp

#include <iostream>
#include <cstring>
using namespace std;

class Gun
{
private:
	int bullet;
public:
	Gun(int bnum): bullet(bnum)
	{}
	void Shot()
	{
		cout<<"빵야!"<<endl;
		bullet--;
	}
};

class Police: public Gun
{
private:
	int handcuffs;
public:
	Police(int bnum, int bcuff): Gun(bnum), handcuffs(bcuff)
	{}
	void PutHandcuff()
	{
		cout<<"Snap!"<<endl;
		handcuffs--;
	}
};

int main(void)
{
	Police pman(5,3);
	pman.Shot();
	pman.PutHandcuff();
	return 0;
}
