//FruitSaleSim3.cpp

#include <iostream>
using namespace std;

class FruitSeller
{
private:
	const int APPLE_PRICE;
	int numOfApples;
	int myMoney;

public:
	FruitSeller (int price, int num, int money): APPLE_PRICE(price), numOfApples(num), myMoney(money)
	{
	}
	
	int SaleApples(int money)
	{
		int num=money/APPLE_PRICE;
		numOfApples -= num;
		myMoney += money;
		return num;
	}
	void ShowSalesResult() const
	{
		cout<<"남은 사과: "<<numOfApples<<endl;
		cout<<"판매 수익: "<<myMoney<<endl<<endl;
	}
};

class FruitBuyer
{
	int myMoney;		//위에 private 선언 안 해도 default로 private로 인식
	int numOfApples;

public:
	FruitBuyer(int money):myMoney(money), numOfApples(0)
	{
	}
	void BuyApples(FruitSeller &seller, int money)
	{
		numOfApples += seller.SaleApples(money);
		myMoney -= money;
	}
	void ShowBuyResult() const
	{
		cout<<"current balance: "<<myMoney<<endl;
		cout<<"num of apples: "<<numOfApples<<endl<<endl;
	}
};

int main(void)
{
	FruitSeller seller(1000, 20, 0);
	FruitBuyer buyer(5000);
	buyer.BuyApples(seller, 2000);	//와... 너무 멋있어...! (감탄)(감탄)

	cout<<"fruit seller status"<<endl;
	seller.ShowSalesResult();
	cout<<"fruit buyer status"<<endl;
	buyer.ShowBuyResult();

	return 0;
}
