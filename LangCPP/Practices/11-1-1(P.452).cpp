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

class Police
{
private:
	int handcuffs;
	Gun * pistol;	//소유한 권총
public:
	Police(int bnum, int bcuff): handcuffs(bcuff)
	{
		if(bnum>0)
			pistol = new Gun(bnum);
		else
			pistol = NULL;
	}
	Police(const Police& pol): handcuffs(pol.handcuffs)	//복사 생성자
	{
		if(pol.pistol==NULL)
			pistol=NULL;
		else
			pistol = new Gun(*(pol.pistol));
	}
	void PutHandcuff()
	{
		cout<<"Snap!"<<endl;
		handcuffs--;
	}
	void Shot()
	{
		if(pistol==NULL)
			cout<<"헛방!"<<endl;
		else
			pistol->Shot();
	}
	~Police()
	{
		delete pistol;
	}
	Police& operator=(const Police& pol)	//대입 연산자
	{
		if(pistol != NULL)
			delete pistol;
		
		if(pol.pistol != NULL)
			pistol = new Gun(*pol.pistol);
		else
			pistol = NULL;
		handcuffs = pol.handcuffs;
		return *this;
	}
};

int main(void)
{
	Police pman1 (5,3);
	pman1.Shot();
	pman1.PutHandcuff();

	Police pman2 (0,3);
	pman2.Shot();
	pman2.PutHandcuff();
	return 0;
}
