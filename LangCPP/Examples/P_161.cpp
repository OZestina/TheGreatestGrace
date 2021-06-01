//Encaps1.cpp

#include <iostream>
using namespace std;

class SinivelCap
{
public:
	void Take() const {cout<<"콧물 멈춰!"<<endl;}
};

class SneezeCap
{
public:
	void Take() const {cout<<"재채기 멈춰!"<<endl;}
};

class SnuffleCap
{
public:
	void Take() const {cout<<"코막힘 멈춰!"<<endl;}
};

class ColdPatient
{
public:
	void TakeSinivelCap(const SinivelCap &cap) const {cap.Take();}
	void TakeSnuffleCap(const SnuffleCap &cap) const {cap.Take();}
	void TakeSneezeCap(const SneezeCap &cap) const {cap.Take();}
};

int main(void)
{
	SinivelCap scap;
	SneezeCap zcap;
	SnuffleCap ncap;

	ColdPatient sufferer;
	sufferer.TakeSinivelCap(scap);
	sufferer.TakeSneezeCap(zcap);
	sufferer.TakeSnuffleCap(ncap);
	return 0;
}
