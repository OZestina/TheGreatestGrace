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
	Book(const Book& ref): price(ref.price)
	{
		title = new char[strlen(ref.title)+1];
		isbn = new char[strlen(ref.isbn)+1];
		strcpy(title, ref.title);
		strcpy(isbn, ref.isbn);
	}
	Book& operator=(const Book& ref)
	{
		delete []title;
		delete []isbn;

		title = new char[strlen(ref.title)+1];
		isbn = new char[strlen(ref.isbn)+1];
		strcpy(title, ref.title);
		strcpy(isbn, ref.isbn);
		price = ref.price;
		return *this;
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
	//test
	EBook(const EBook& ref): Book(ref)
	{
		DRMKey = new char[strlen(ref.DRMKey)+1];
		strcpy(DRMKey, ref.DRMKey);
	}
	EBook& operator=(const EBook& ref)
	{
		Book::operator=(ref);
		delete []DRMKey;
		DRMKey = new char[strlen(ref.DRMKey)+1];
		strcpy(DRMKey, ref.DRMKey);
		return *this;
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
	EBook ebook1("좋은 c++", "555-12345-890-0", 20000, "12345");
	EBook ebook2 = ebook1;
	ebook2.ShowEBookInfo();
	cout<<endl;
	
	EBook ebook3("dummy", "1", 0, "1");
	ebook3 = ebook1;
	ebook3.ShowEBookInfo();
	return 0;
}
