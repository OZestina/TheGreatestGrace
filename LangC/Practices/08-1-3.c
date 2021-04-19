#include <stdio.h>

int main(void)
{
	char grade;
	int kor, eng, math;
	double ave;

	printf("국어 점수를 입력하세요: ");
	scanf("%d", &kor);
	printf("영어 점수를 입력하세요: ");
	scanf("%d", &eng);
	printf("수학 점수를 입력하세요: ");
	scanf("%d", &math);

	ave = ((double)kor+eng+math)/3;

	if(ave>=90)
		grade = 'A';
	else if(ave>=80)
		grade = 'B';
	else if(ave>=70)
		grade = 'C';
	else if(ave>=50)
		grade = 'D';
	else
		grade = 'F';

	printf("당신의 평균은 %f, 학점은 %c입니다.\n", ave, grade);

	return 0;
}
