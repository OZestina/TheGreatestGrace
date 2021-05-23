#include <iostream>
int BoxVolumn(int length, int width, int height);
int BoxVolumn(int length, int width);
int BoxVolumn(int length);

int main(void)
{
	std::cout<<"[3,3,3]: "<<BoxVolumn(3,3,3)<<std::endl;
	std::cout<<"[5,5,D]: "<<BoxVolumn(5,5)<<std::endl;
	std::cout<<"[7,D,D]: "<<BoxVolumn(7)<<std::endl;
	return 0;
}

int BoxVolumn(int length, int width, int height)
{
	return length*width*height;
}

int BoxVolumn(int length, int width)
{
	return length*width;
}

int BoxVolumn(int length)
{
	return length;
}
