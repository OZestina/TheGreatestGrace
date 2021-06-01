//const함수로 안전성을 높여보자~

#include <iostream>
using namespace std;

class FruitSeller
{
private:
	int APPLE_PRICE;
	int numOfApples;
	int myMoney;

public:
	void InitMembers(int price, int num, int money)
	{
		APPLE_PRICE = price;	//바뀌지 않는 변수여서 모두 대문자로 표기 (상수)
		numOfApples = num;
		myMoney = money;
	}
	
	int SaleApples(int money)
	{
		if(money<0)	//if절 추가
		{
			cout<<"input money more than 0"<<endl;
			return 0;
		}
		int num=money/1000;
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
	void InitMembers(int money)
	{
		myMoney = money;
		numOfApples = 0;
	}
	void BuyApples(FruitSeller &seller, int money)
	{
		if (money<0)
		{
			cout<<"input money more than 0"<<endl;
			return;
		}
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
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	buyer.BuyApples(seller, 2000);

	cout<<"fruit seller status"<<endl;
	seller.ShowSalesResult();
	cout<<"fruit buyer status"<<endl;
	buyer.ShowBuyResult();

	return 0;
}
