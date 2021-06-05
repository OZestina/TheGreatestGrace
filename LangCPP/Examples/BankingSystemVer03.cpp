//P_240

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

class Account
{
private:
	int accountID;
	char * name;
	int balance;
public:
	Account(int ID, char *_name, int money): accountID(ID), balance(money)
	{
		name = new char(strlen(_name)+1);
		strcpy(name, _name);
	}

	Account(Account &ref): accountID(ref.accountID), balance(ref.balance)
	{
		name = new char(strlen(ref.name)+1);
		strcpy(name, ref.name);
	}

	int GetAccID() { return accountID; }	//클래스 변수가 private로 정의되면 함수를 통해서만 접근이 가능하므로

	void Deposit(int money)
	{
		balance += money;
	}

	int Withdraw(int money)
	{
		if(money>balance)	//잔고가 0보다 작아질 경우 0 반환
			return 0;
		balance -= money;
		return money;
	}
	void ShowAccInfo()
	{
		cout<<"계좌ID: "<<accountID<<endl;
		cout<<"이름: "<<name<<endl;
		cout<<"잔액: "<<balance<<endl;
	}
	~Account()
	{
		delete []name;
	}
};

Account * accArr[100];	//account 저장을 위한 포인트 배열
int accNum=0;	//저장된 account 수

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
			for(int i=0; i<accNum; i++)
				delete accArr[i];
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
	cout<<"계좌ID: "; cin>>ID;
	cout<<"이름: ";	cin>>name;
	cout<<"입금액: "; cin>>balance;
	cout<<endl;

	accArr[accNum] = new Account(ID, name, balance);
	accNum++;
}

void DepositMoney(void)
{
	int money;
	int id;

	cout<<"[입금]\n";
	cout<<"계좌ID: "; cin>>id;
	cout<<"입금액: "; cin>>money;

	for(int i=0; i<accNum; i++)
	{
		if(accArr[i]->GetAccID()==id)
		{
			accArr[i]->Deposit(money);
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
		if(accArr[i]->GetAccID()==id)
		{
			if(accArr[i]->Withdraw(money)==0)
			{
				cout<<"잔액부족"<<endl<<endl;
				return;
			}
			cout<<"출금완료\n\n";
			return;
		}
	}
	cout<<"유효하지 않은 ID입니다."<<endl<<endl;
}

void ShowAllAccInfo(void)
{
	cout<<"[전체 계좌 출력]"<<endl;
	for(int i=0; i<accNum; i++)
	{
		accArr[i]->ShowAccInfo();
		cout<<endl;
	}
}
