//StringClass.cpp

#include <iostream>
#include <cstring>
using namespace std;

class String
{
private:
	int len;
	char * str;
public:
	String()
	{
		len = 0;
		str = NULL;
	}
	String(char * s)
	{
		len=strlen(s)+1;
		str = new char[len];
		strcpy(str,s);
	}
	String(const String& ref)
	{
		len=ref.len;
		str = new char[len];
		strcpy(str, ref.str);
	}
	~String()
	{
		if(str!=NULL)
			delete []str;
	}

	String& operator= (const String& ref)
	{
		if(str!=NULL)
			delete []str;
		str = new char[len];
		strcpy(str, ref.str);
		len=ref.len;
		return *this;
	}

	String& operator+= (const String& ref)
	{
		len+=(ref.len-1);
		char* tempstr = new char[len];
		strcpy(tempstr,str);
		strcat(tempstr,ref.str);

		if(str!=NULL)
			delete []str;
		str = tempstr;
		return *this;
	}

	bool operator==(const String& s)
	{
		return strcmp(str, s.str)? false: true;
	}

	String operator+ (const String& ref)
	{
		char* tempstr = new char[len+ref.len-1];
		strcpy(tempstr,str);
		strcat(tempstr,ref.str);

		String temp(tempstr);
		delete []tempstr;
		return temp;
	}

	friend ostream& operator<< (ostream& os, const String& ref);
	friend istream& operator>> (istream& is, String& s);
};

ostream& operator<< (ostream& os, const String& ref)
{
	os<<ref.str;
	return os;
}

istream& operator>> (istream& is, String& s)
{
	char str[100];
	is>>str;
	s=String(str);
	return is;
}
