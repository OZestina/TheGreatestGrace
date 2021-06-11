//Account.h
#ifndef __ACCOUNT_H__
#define __ACCOUNT_H__

class Account
{
private:
	int accountID;
	char * name;
	int balance;
public:
	Account(int ID, char *_name, int money);
	Account(const Account &ref);

	int GetAccID() const;
	virtual void Deposit(int money);
	int Withdraw(int money);
	virtual void ShowAccInfo() const;
	~Account();

	friend Account& operator= (const Account& acc);
};

#endif






//Account.cpp
#include "Account.h"
#include "BankingCommonDecl.h"

Account::Account(int ID, char *_name, int money): accountID(ID), balance(money)
{
	name = new char(strlen(_name)+1);
	strcpy(name, _name);
}

Account::Account(const Account &ref): accountID(ref.accountID), balance(ref.balance)
{
	name = new char(strlen(ref.name)+1);
	strcpy(name, ref.name);
}

int Account::GetAccID() const { return accountID; }	//클래스 변수가 private로 정의되면 함수를 통해서만 접근이 가능하므로

void Account::Deposit(int money)
{
	balance += money;
}

int Account::Withdraw(int money)
{
	if(money>balance)	//잔고가 0보다 작아질 경우 0 반환
		return 0;
	balance -= money;
	return money;
}

void Account::ShowAccInfo() const
{
	cout<<"계좌ID: "<<accountID<<endl;
	cout<<"이름: "<<name<<endl;
	cout<<"잔액: "<<balance<<endl;
}

Account::~Account()
{
	delete []name;
}

Account& Account::operator= (const Account& ref)
{
	accountID = ref.accountID;
	balance = ref.balance;

	delete []name;
	name = new char(strlen(ref.name)+1);
	strcpy(name, ref.name);
	return *this;
}






//AccountHandler.h
#ifndef __ACCOUNT_HANDLER_H__
#define __ACCOUNT_HANDLER_H__

#include "Account.h"
#include "AccountArray.h"

class AccountHandler	//control 클래스
{
public:
	BoundCheckAccountPtrArray accArr;	//account 저장을 위한 포인트 배열
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








//AccountArray.h
#ifndef __ACCOUNT_ARRAY_H__
#define __ACCOUNT_ARRAY_H__

#include "Account.h"
typedef Account* ACCOUNT_PTR;

class BoundCheckAccountPtrArray
{
private:
	ACCOUNT_PTR * arr;
	int arrlen;
	BoundCheckAccountPtrArray(const BoundCheckAccountPtrArray& arr) {}
	BoundCheckAccountPtrArray& operator=(const BoundCheckAccountPtrArray& arr) {}

public:
	BoundCheckAccountPtrArray(int len=100);
	ACCOUNT_PTR& operator[](int idx);
	ACCOUNT_PTR operator[](int idx) const;
	int GetArrLen() const ;
	~BoundCheckAccountPtrArray();
};

#endif








//AccountArray.cpp
#include "AccountArray.h"
#include "BankingCommonDecl.h"

BoundCheckAccountPtrArray::BoundCheckAccountPtrArray(int len): arrlen(len)
{
	arr = new ACCOUNT_PTR[len];
}

ACCOUNT_PTR& BoundCheckAccountPtrArray::operator[](int idx)
{
	if(idx<0 || idx>=arrlen)
	{
		cout<<"Array index out of bound exception"<<endl;
		exit(1);
	}
	return arr[idx];
}

ACCOUNT_PTR BoundCheckAccountPtrArray::operator[](int idx) const
{
	if(idx<0 || idx>=arrlen)
	{
		cout<<"Array index out of bound exception"<<endl;
		exit(1);
	}
	return arr[idx];
}

int BoundCheckAccountPtrArray::GetArrLen() const 
{ return arrlen; }

BoundCheckAccountPtrArray::~BoundCheckAccountPtrArray() 
{ delete []arr; }







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
