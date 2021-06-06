//StaticMember.cpp

#include <iostream>
using namespace std;

class SoSimple
{
private:
	static int simObjCnt;
public:
	SoSimple()
	{
		simObjCnt++;
		cout<<simObjCnt<<"번째 SoSimple 객체"<<endl;
	}
};
int SoSimple::simObjCnt = 0;	//class static 변수 초기화 방법

class SoComplex
{
private:
	static int cmxObjCnt;

public:
	SoComplex()
	{
		cmxObjCnt++;
		cout<<cmxObjCnt<<"번째 So Complex 객체"<<endl;
	}
	SoComplex(SoComplex &copy)
	{
		cmxObjCnt++;
		cout<<cmxObjCnt<<"번째 So Complex 객체"<<endl;
	}
};
int SoComplex::cmxObjCnt = 0;

int main(void)
{
	SoSimple sim1;
	SoSimple sim2;

	SoComplex com1;
	SoComplex com2=com1;
	SoComplex();

	return 0;
}
