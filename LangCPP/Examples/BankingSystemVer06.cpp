#include <iostream>
#include <cstring>

using namespace std;
const int NAME_LEN=20;

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

	Account(const Account &ref): accountID(ref.accountID), balance(ref.balance)
	{
		name = new char(strlen(ref.name)+1);
		strcpy(name, ref.name);
	}

	int GetAccID() const { return accountID; }	//클래스 변수가 private로 정의되면 함수를 통해서만 접근이 가능하므로

	virtual void Deposit(int money)
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
	virtual void ShowAccInfo() const
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

class NormalAccount : public Account
{
private:
	int interest;
public:
	NormalAccount(int ID, char *_name, int money, int inter): Account(ID, _name, money), interest(inter)
	{ }
	int GetInterest() const
	{
		return interest;
	}
	virtual int DepositMoney (int money)
	{
		return money + (int)(money*(interest)/100);
	}
	virtual void Deposit(int money)
	{
		Account::Deposit(DepositMoney(money));
	}
};

namespace ACC_LEVEL
{
	enum { A = 1, B, C };
}

class HighCreditAccount : public NormalAccount
{
private:
	int level;
public:
	HighCreditAccount(int ID, char *_name, int money, int inter, int lev) : NormalAccount(ID, _name, money, inter), level(lev)
	{ }
	virtual int DepositMoney (int money)
	{
		int rate;
		if(level==1)
			rate = 7;
		else if(level==2)
			rate = 4;
		else if(level==3)
			rate = 2;

		return money + (int)(money*(rate + NormalAccount::GetInterest())/100);
	}
	virtual void Deposit(int money)
	{
		Account::Deposit(DepositMoney(money));
	}
};

class AccountHandler	//control 클래스
{
public:
	Account * accArr[100];	//account 저장을 위한 포인트 배열
	int accNum;		//저장된 account 수
public:
	AccountHandler(): accNum(0)
	{}
	
	~AccountHandler()
	{
		for(int i=0; i<accNum; i++)
			delete accArr[i];
	}

	void MenuOut(void) const
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

	int MakeAccountMenu(void)
	{
		int n;
		cout<<"[계좌종류선택]"<<endl;
		cout<<"1.보통예금계좌 2.신용신뢰계좌"<<endl;
		cin>>n;
		return n;
	}

	void MakeAccount_Normal(void)
	{
		int ID;
		char name[NAME_LEN];
		int balance;
		int inter;
		//NormalAccount(int ID, char *_name, int money, int inter)

		cout<<"[계좌개설]\n";
		cout<<"계좌ID: "; cin>>ID;
		cout<<"이름: ";	cin>>name;
		cout<<"입금액: "; cin>>balance;
		cout<<"이자율: "; cin>>inter;
		cout<<endl;

		accArr[accNum] = new NormalAccount(ID, name, balance, inter);
		accNum++;
	}

	void MakeAccount_Credit(void)
	{
		int ID;
		char name[NAME_LEN];
		int balance;
		int inter;
		int level;
		//HighCreditAccount(int ID, char *_name, int money, int inter, int lev)

		cout<<"[계좌개설]\n";
		cout<<"계좌ID: "; cin>>ID;
		cout<<"이름: ";	cin>>name;
		cout<<"입금액: "; cin>>balance;
		cout<<"이자율: "; cin>>inter;
		cout<<"신용등급(1toA, 2toB, 3toC): "; cin>>level;
		cout<<endl;

		accArr[accNum] = new HighCreditAccount(ID, name, balance, inter, level);
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
};

int main(void)
{
	AccountHandler manager;
	int choice =0;

	while(1)
	{
		manager.MenuOut();
		choice=manager.MenuIn();

		switch(choice)
		{
		case MAKE:
		{
			int m = 0;
			m = manager.MakeAccountMenu();
			if (m==1)
				manager.MakeAccount_Normal();
			else if (m==2)
				manager.MakeAccount_Credit();
			else
				cout<<"Illegal selection..."<<endl;
			break;
		}	
		case DEPOSIT:
			manager.DepositMoney();
			break;
		case WITHDRAW:
			manager.WithdrawMoney();
			break;
		case INQUIRE:
			manager.ShowAllAccInfo();
			break;
		case EXIT:
			return 0;
		default:
			cout<<"Illegal selection..."<<endl;
		}
	}
	return 0;
}
