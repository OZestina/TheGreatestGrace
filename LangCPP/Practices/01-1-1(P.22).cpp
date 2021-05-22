#include <iostream>

int main(void)
{
	int num[5];
	int sum=0;

	for(int i=0; i<5; i++)
	{
		std::cout<<i+1<<"번째 정수 입력: ";
		std::cin>>num[i];
		sum+=num[i];
	}
	
	std::cout<<"합계: "<<sum<<std::endl;
	
	return 0;
}

//굳이 5개의 정수를 따로 입력할 필요는 없어서 (합계만 나오면 되니) 하기와 같이도 가능하다 (메모리를 덜씀)
#include <iostream>

int main(void)
{
	int input;
	int sum=0;

	for(int i=0; i<5; i++)
	{
		std::cout<<i+1<<"번째 정수 입력: ";
		std::cin>>input;
		sum+=input;
	}
	
	std::cout<<"합계: "<<sum<<std::endl;
	
	return 0;
}
