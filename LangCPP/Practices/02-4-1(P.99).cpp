#include <iostream>
#include <cstring>
using namespace std;

int main(void)
{
	char * str1 = "Hello, world!";
	char str2[30];
	int a;
	strcpy(str2, str1);
	strcat(str2, " It's me, again");
	a = strcmp(str1, str2);

	cout<<"str1의 길이: "<<strlen(str1)<<endl;
	cout<<"str2: "<<str2<<endl;
	
	if(a == 0)
		cout<<"문장이 같습니다"<<endl;
	else if (a<0)
		cout<<"str1이 더 짧습니다"<<endl;
	else
		cout<<"str1이 더 깁니다"<<endl;

	return 0;
}
