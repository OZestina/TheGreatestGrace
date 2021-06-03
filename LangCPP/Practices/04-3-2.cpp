#include <iostream>
#include <cstring>
using namespace std;

namespace COMP_POS
{
	enum {CLERK, SENIOR, ASSIST, MANAGER};

	void ShowPositionInfo(int pos)
	{
		switch(pos)
		{
		case CLERK:
			cout<<"사원"<<endl;
			break;
		case SENIOR:
			cout<<"주임"<<endl;
			break;
		case ASSIST:
			cout<<"대리"<<endl;
			break;
		case MANAGER:
			cout<<"과장"<<endl;
			break;
		}
	}
}

class NameCard
{
private:
	char * name;
	char * company;
	char * phone;
	int position;
public:
	NameCard(char* _name, char* _company, char* _phone, int pos)
	{
		name = new char[strlen(_name)+1];
		company = new char[strlen(_company)];
		phone = new char[strlen(_phone)];

		strcpy(name, _name);
		strcpy(company, _company);
		strcpy(phone, _phone);
		position = pos;
	}
	void ShowNameCardInfo()
	{
		cout<<"이름: "<<name<<endl;
		cout<<"회사: "<<company<<endl;
		cout<<"전화번호: "<<phone<<endl;
		cout<<"직급: ";
		COMP_POS::ShowPositionInfo(position);
		cout<<endl<<endl;
	}
};

int main(void)
{
	NameCard manClerk("Lee", "ABCEng", "010-1111-2222", COMP_POS::CLERK);
	NameCard manSENIOR("Hong", "Orange", "010-3333-4444", COMP_POS::SENIOR);
	NameCard manASSIST("Kim", "SoGood", "010-1111-7777", COMP_POS::ASSIST);

	manClerk.ShowNameCardInfo();
	manSENIOR.ShowNameCardInfo();
	manASSIST.ShowNameCardInfo();
	return 0;
}
