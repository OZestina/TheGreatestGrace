#include <iostream>
#include <cstring>
using namespace std;

class MyFriendInfo
{
private:
	char * name;
	int age;
public:
	MyFriendInfo(char * myname, int myage): age(myage)
	{
		name = new char[strlen(myname)+1];
		strcpy(name, myname);
	}
	~MyFriendInfo()
	{
		delete []name;
	}
	void ShowMyFriendInfo()
	{
		cout<<"Name: "<<name<<endl;
		cout<<"Age: "<<age<<endl;
	}
};

class MyFriendDetailInfo : public MyFriendInfo
{
private:
	char * addr;
	char * phone;
public:
	MyFriendDetailInfo(char * myname, int myage, char *myaddr, char *myphone): MyFriendInfo(myname, myage)
	{
		addr = new char[strlen(myaddr)+1];
		strcpy(addr, myaddr);
		phone = new char[strlen(myphone)+1];
		strcpy(phone, myphone);
	}
	~MyFriendDetailInfo()
	{
		delete []addr;
		delete []phone;
	}
	void ShowMyFriendDetailInfo()
	{
		ShowMyFriendInfo();
		cout<<"Address: "<<addr<<endl;
		cout<<"Phoen #: "<<phone<<endl<<endl;
	}
};

int main(void)
{
	MyFriendDetailInfo friend1("Kim", 28, "Gangnam", "010-1111-2222");
	MyFriendDetailInfo friend2("Lee", 35, "Seocho", "010-1234-3456");

	friend1.ShowMyFriendDetailInfo();
	friend2.ShowMyFriendDetailInfo();

	friend1.ShowMyFriendInfo();
	return 0;
}
