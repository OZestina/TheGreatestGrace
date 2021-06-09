//P_053

#include <iostream>
#include <cstring>

using namespace std;
const int NAME_LEN=20;

void MenuOut(void);	//메뉴 출력
int MenuIn(void);	//메뉴 선택
void MakeAccount(void);
void DepositMoney(void);
void WithdrawMoney(void);
void ShowAllAccInfo(void);

enum {MAKE=1, DEPOSIT, WITHDRAW, INQUIRE, EXIT};

typedef struct memInfo
{
	int accountID;
	char name[NAME_LEN];
	int balance;
}MemInfo;

MemInfo memArr[100];	//전역변수로 하면 다 0으로 초기화
int accNum=0;	//저장된 member 수

int main(void)
{
	int choice =0;

	while(1)
	{
		MenuOut();
		choice=MenuIn();

		switch(choice)
		{
		case MAKE:
			MakeAccount();
			break;
		case DEPOSIT:
			DepositMoney();
			break;
		case WITHDRAW:
			WithdrawMoney();
			break;
		case INQUIRE:
			ShowAllAccInfo();
			break;
		case EXIT:
			return 0;
		default:
			cout<<"Illegal selection..."<<endl;
		}
	}
	return 0;
}

void MenuOut(void)
{
	cout<<"-----Menu----\n";
	cout<<"1. 계좌개설\n";
	cout<<"2. 입 금\n";
	cout<<"3. 출 금\n";
	cout<<"4. 계좌정보 전체 출력\n";
	cout<<"5. 프로그램 종료\n"<<"선택: ";
}

int MenuIn(void)
{
	int n;
	cin>>n;
	return n;
}

void MakeAccount(void)
{
	int ID;
	char name[NAME_LEN];
	int balance;

	cout<<"[계좌개설]\n";
	cout<<"계좌ID: ";
	cin>>ID;
	cout<<"이름: ";
	cin>>name;
	cout<<"입금액: ";
	cin>>balance;

	memArr[accNum].accountID = ID;
	memArr[accNum].balance = balance;
	strcpy(memArr[accNum].name, name);  //name 주소값에 저장된 문자열을 memArr[accNum].name로 복사
	accNum++;
}

void DepositMoney(void)
{
	int money;
	int id;

	cout<<"[입금]\n";
	cout<<"계좌ID: ";
	cin>>id;
	cout<<"입금액: ";
	cin>>money;

	for(int i=0; i<accNum; i++)
	{
		if(id == memArr[i].accountID)
		{
			memArr[i].balance += money;
			cout<<"입금완료\n\n";
			return;
		}
	}
	cout<<"유효하지 않은 ID입니다."<<endl<<endl;
}

void WithdrawMoney(void)
{
	int id;
	int money;

	cout<<"[출금]\n";
	cout<<"계좌ID: "; cin>>id;
	cout<<"출금액: "; cin>>money;
	
	for(int i=0; i<accNum; i++)
	{
		if(id==memArr[i].accountID)
		{
			if(memArr[i].balance<money)
			{
				cout<<"잔액부족"<<endl<<endl;
				return;
			}

			memArr[i].balance -= money;
			cout<<"출금완료\n\n";
			return;
		}
	}
	cout<<"유효하지 않은 ID입니다."<<endl<<endl;
}

void ShowAllAccInfo(void)
{
	for(int i=0; i<accNum; i++)
	{
		if(memArr[i].accountID!=0)
		{
			cout<<"계좌ID: "<<memArr[i].accountID<<endl;
			cout<<"이름: "<<memArr[i].name<<endl;
			cout<<"잔액: "<<memArr[i].balance<<endl<<endl;
			return;
		}
	}
	cout<<"생성된 계좌가 없습니다."<<endl<<endl;
}
