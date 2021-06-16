//AccountException.h
#ifndef __ACCOUNT_EXCEPTION_H__
#define __ACCOUNT_EXCEPTION_H__

class MinusException
{
private:
	int exval;
public:
	MinusException(int money): exval(money) { }
	void ShowExceptionInfo() const
	{
		cout<<"입(출)금액 "<<exval<<"은 유효하지 않습니다."<<endl;
	}
};

class InsuffException
{
private:
	int balance;
	int reqval;
public:
	InsuffException(int bal, int money): balance(bal), reqval(money) { }
	void ShowExceptionInfo() const
	{
		cout<<"잔액에서 "<<reqval-balance<<"가(이) 부족합니다."<<endl;
	}
};

#endif

//String.h
#ifndef __STRING_H__
#define __STRING_H__

#include "BankingCommonDecl.h"

class String
{
private:
	int len;
	char * str;
public:
	String();
	String(const char*s);
	String(const String& s);
	~String();

	String& operator= (const String& s);
	String& operator+= (const String& s);
	bool operator== (const String& s);
	String operator+ (const String& s);

	friend ostream& operator<< (ostream& os, const String& s);
	friend istream& operator>> (istream& is, String& s);
};

#endif

//String.cpp

String::String()
{
	len = 0;
	str = NULL;
}
String::String(const char*s)
{
	len = strlen(s)+1;
	str = new char[len];
	strcpy(str, s);
}
String::String(const String& s)
{
	len = s.len;
	str = new char[len];
	strcpy(str,s.str);
}
String::~String()
{
	if(str!=NULL)
		delete []str;
}

String& String::operator= (const String& s)
{
	if(str!=NULL)
		delete []str;
	len=s.len;
	str = new char[len];
	strcpy(str,s.str);
	return *this;
}

String& String::operator+= (const String& s)
{
	len+=(s.len-1);
	char * tempstr = new char[len];
	strcpy(tempstr, str);
	strcat(tempstr, s.str);

	if(str!=NULL)
		delete []str;
	str = tempstr;
	return *this;
}

bool String::operator== (const String& s)
{
	return strcmp(str, s.str) ? false : true;
}
String String::operator+ (const String& s)
{
	char * strtemp = new char[len+s.len-1];
	strcpy(strtemp, str);
	strcat(strtemp, s.str);

	String temp(strtemp);	//String::String(const char*s) 사용!
	delete []strtemp;
	return temp;
}

ostream& operator<< (ostream& os, const String& s)
{
	os<<s.str;
	return os;
}
istream& operator>> (istream& is, String& s)
{
	char str[100];
	cin>>str;
	s=String(str);	//String::String(const char*s) 사용!
	return is;
}


//Account.h
#ifndef __ACCOUNT_H__
#define __ACCOUNT_H__

#include "String.h"

class Account
{
private:
	int accountID;
	int balance;
	String name;
public:
	Account(int ID, String name, int money);

	int GetAccID() const;
	virtual void Deposit(int money);
	int Withdraw(int money);
	virtual void ShowAccInfo() const;
};

#endif






//Account.cpp
#include "Account.h"
#include "BankingCommonDecl.h"
#include "AccountException.h"

Account::Account(int ID, String name, int money): accountID(ID), balance(money)
{
	this->name = name;
}

int Account::GetAccID() const { return accountID; }	//클래스 변수가 private로 정의되면 함수를 통해서만 접근이 가능하므로

void Account::Deposit(int money)
{	
	if (money<0)
		throw MinusException(money);

	balance += money;
}

int Account::Withdraw(int money)
{
	if(money<0)
		throw MinusException(money);
	
	if(money>balance)
		throw InsuffException(balance, money);

	balance -= money;
	return money;
}

void Account::ShowAccInfo() const
{
	cout<<"계좌ID: "<<accountID<<endl;
	cout<<"이름: "<<name<<endl;
	cout<<"잔액: "<<balance<<endl;
}






//NormalAccout.h (함수 정의도 cpp분할 없이 헤더에 모두 저장 - 양이 적으니까!)

#ifndef __NORMAL_ACCOUNT_H__
#define __NORMAL_ACCOUNT_H__

#include "Account.h"
#include "String.h"
#include "AccountException.h"

class NormalAccount : public Account
{
private:
	int interest;
public:
	NormalAccount(int ID, String _name, int money, int inter): Account(ID, _name, money), interest(inter)
	{ }
	virtual void Deposit(int money)
	{
		if(money<0)
			throw MinusException(money);
		
		Account::Deposit(money);
		Account::Deposit(money*(interest/100.0));
	}
};

#endif







//HighCreditAccount.h

#ifndef __HIGHCREDIT_ACCOUNT_H__
#define __HIGHCREDIT_ACCOUNT_H__

#include "NormalAccount.h"
#include "String.h"

class HighCreditAccount : public NormalAccount
{
private:
	int level;
public:
	HighCreditAccount(int ID, String _name, int money, int inter, int lev) : NormalAccount(ID, _name, money, inter), level(lev)
	{ }
	
	virtual void Deposit(int money)
	{
		if(money<0)
			throw MinusException(money);

		NormalAccount::Deposit(money);	//원금과 이자추가
		Account::Deposit(money*(level/100.0));	//특별이자추가
	}
};

#endif




//BoundCheckArray.h
#ifndef __BOUND_CHECK_ARRAY_H__
#define __BOUND_CHECK_ARRAY_H__

#include "BankingCommonDecl.h"

template <typename T>
class BoundCheckArray
{
private:
	T* arr;
	int arrlen;
	BoundCheckArray(const BoundCheckArray& arr) {}
	BoundCheckArray& operator=(const BoundCheckArray& arr) {}
public:
	BoundCheckArray(int len=100): arrlen(len)
	{
		arr = new T[len];
	}
	T& operator[](int idx)
	{
		if(idx<0 || idx>=arrlen)
		{
			cout<<"Array index out of bound exception"<<endl;
			exit(1);
		}
		return arr[idx];
	}

	T operator[](int idx) const
	{
		{
		if(idx<0 || idx>=arrlen)
		{
			cout<<"Array index out of bound exception"<<endl;
			exit(1);
		}
		return arr[idx];
	}
	
	int GetArrLen() const 
	{ return arrlen; }

	~BoundCheckArray()
	{ delete []arr; }
};

#endif





//AccountHandler.h

#ifndef __ACCOUNT_HANDLER_H__
#define __ACCOUNT_HANDLER_H__

#include "Account.h"
#include "BoundCheckArray.h"

class AccountHandler	//control 클래스
{
public:
	BoundCheckArray<Account*> accArr;	//account 저장을 위한 포인트 배열
	int accNum;		//저장된 account 수
public:
	AccountHandler();
	~AccountHandler();
	void MenuOut(void) const;
	int MenuIn(void);
	void MakeAccount(void);
	void DepositMoney(void);
	void WithdrawMoney(void);
	void ShowAllAccInfo(void);
protected:
	void MakeAccount_Normal(void);
	void MakeAccount_Credit(void);
};

#endif





//AccountHandler.cpp

#include "Account.h"
#include "BankingCommonDecl.h"
#include "NormalAccount.h"
#include "HighCreditAccount.h"
#include "AccountHandler.h"
#include "String.h"

AccountHandler::AccountHandler(): accNum(0)
{}
	
AccountHandler::~AccountHandler()
{
	for(int i=0; i<accNum; i++)
		delete accArr[i];
}

void AccountHandler::MenuOut(void) const
{
	cout<<"-----Menu----\n";
	cout<<"1. 계좌개설\n";
	cout<<"2. 입 금\n";
	cout<<"3. 출 금\n";
	cout<<"4. 계좌정보 전체 출력\n";
	cout<<"5. 프로그램 종료\n"<<"선택: ";
}

int AccountHandler::MenuIn(void)
{
	int n;
	cin>>n;
	return n;
}

void AccountHandler::MakeAccount(void)
{
	int n;
	cout<<"[계좌종류선택]"<<endl;
	cout<<"1.보통예금계좌 2.신용신뢰계좌"<<endl;
	cin>>n;
		
	if(n==NORMAL)
		MakeAccount_Normal();
	else if(n==CREDIT)
		MakeAccount_Credit();
}

void AccountHandler::DepositMoney(void)
{
	int money;
	int id;

	cout<<"[입금]\n";
	cout<<"계좌ID: "; cin>>id;
	
	while(true)
	{
		cout<<"입금액: "; cin>>money;

		try
		{
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
			return;
		}
		catch(MinusException& expn)
		{
			expn.ShowExceptionInfo();
			cout<<"입금액만 재입력하세요."<<endl;
		}
	}
}

void AccountHandler::WithdrawMoney(void)
{
	int id;
	int money;

	cout<<"[출금]\n";
	cout<<"계좌ID: "; cin>>id;

	while(1)
	{
		cout<<"출금액: "; cin>>money;
		try
		{
			for(int i=0; i<accNum; i++)
			{
				if(accArr[i]->GetAccID()==id)
				{
					if(accArr[i]->Withdraw(money);
					cout<<"출금완료\n\n";
					return;
				}
			}
			cout<<"유효하지 않은 ID입니다."<<endl<<endl;
			return;
		}
		catch(MinusException& expn)
		{
			expn.ShowExceptionInfo();
			cout<<"출금액만 재입력하세요."<<endl;
		}
		catch(InsuffException& expn)
		{
			expn.ShowExceptionInfo();
			cout<<"출금액만 재입력하세요."<<endl;
		}
	}
}

void AccountHandler::ShowAllAccInfo(void)
{
	cout<<"[전체 계좌 출력]"<<endl;
	for(int i=0; i<accNum; i++)
	{
		accArr[i]->ShowAccInfo();
		cout<<endl;
	}
}

void AccountHandler::MakeAccount_Normal(void)
{
	int ID;
	String name;
	//char name[NAME_LEN];
	int balance;
	int inter;
	//NormalAccount(int ID, char *_name, int money, int inter)

	cout<<"[계좌개설]\n";
	cout<<"계좌ID: "; cin>>ID;
	cout<<"이름: ";	cin>>name;	
	cout<<"이자율: "; cin>>inter;
	cout<<endl;

	accArr[accNum] = new NormalAccount(ID, name, balance, inter);
	accNum++;
}

void AccountHandler::MakeAccount_Credit(void)
{
	int ID;
	String name;
	//char name[NAME_LEN];
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

	switch(level)
	{
	case 1:
		accArr[accNum] = new HighCreditAccount(ID, name, balance, inter, LEVEL_A);
		break;
	case 2:
		accArr[accNum] = new HighCreditAccount(ID, name, balance, inter, LEVEL_B);
		break;
	case 3:
		accArr[accNum] = new HighCreditAccount(ID, name, balance, inter, LEVEL_C);
		break;
	}
}






//BankingCommonDecl.h

#ifndef __BANKING_COMMON_H__
#define __BANKING_COMMON_H__

#include <iostream>
#include <cstring>
#include <cstdlib>  //추가됨 (exit 사용을 위해)
using namespace std;

const int NAME_LEN=20;

//선택메뉴
enum {MAKE=1, DEPOSIT, WITHDRAW, INQUIRE, EXIT};
//계좌의 종류
enum {NORMAL=1, CREDIT};
//신용등급
enum {LEVEL_A=7, LEVEL_B=4, LEVEL_C=2};

#endif





//BankingSystemMain.cpp

#include "BankingCommonDecl.h"
#include "AccountHandler.h"

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
			manager.MakeAccount();
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
