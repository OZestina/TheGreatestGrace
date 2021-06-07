#include <iostream>
#include <cstring>
using namespace std;

class Book
{
private:
	char * title;
	char * isbn;
	int price;
public:
	Book(char* t, char*id, int money): price(money)
	{
		title = new char[strlen(t)+1];
		isbn = new char[strlen(id)+1];
		strcpy(title, t);
		strcpy(isbn, id);
	}
	~Book()
	{
		delete []title;	//check this part!
		delete []isbn;
	}
	void ShowBookInfo() const
	{
		cout<<"제목: "<<title<<endl;
		cout<<"ISBN: "<<isbn<<endl;
		cout<<"가격: "<<price<<endl;
	}
};

class EBook : public Book
{
private:
	char * DRMKey;
public:
	EBook(char* t, char*id, int money, char * key): Book(t, id, money)
	{
		DRMKey = new char[strlen(key)+1];
		strcpy(DRMKey, key);
	}
	~EBook()
	{
		delete []DRMKey;
	}
	void ShowEBookInfo() const
	{
		ShowBookInfo();
		cout<<"인증키: "<<DRMKey<<endl;
	}
};

int main(void)
{
	Book book("좋은 c++", "555-12345-890-0", 20000);
	book.ShowBookInfo();
	cout<<endl;
	EBook ebook("좋은 c++ ebook", "555-12345-890-1", 10000, "fdsa1q2w3e3r");
	ebook.ShowEBookInfo();
	return 0;
}
