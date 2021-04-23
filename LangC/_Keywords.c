//C언어에서 이미 기능적인 의미가 정해져 있는 단어들
//대소문자 주의!

auto
_Bool
break //현재 loop를 벗어나라~는 의미
case
char  //문자 데이터 표현을 위해 정의된 자료형 (1바이트)
_Complex
const   //이름을 지니는 심볼릭(symbolic) 상수를 const 상수라 함
        // 1) 'const' 키워드 사용: 변수 선언 시 const 선언 추가 및 선언과 동시에 초기화 (상수이므로!) 초기화되면 값을 변경할 수 "없다"
                                // (관례) 상수의 이름은 모두 대문자로 표기, 띄어쓰기는 언더바(_)로 표시

                #include <stdio.h>
                int main()
                {
                        const int MAX = 100;
                        const double PI_VALUE = 3.1415;
                        return 0;
                }
                
        // 2) 매크로 이용
        
continue  //loop를 지나쳐 계속 실행하라~는 의미
default
do  //do~while문
double  //실수 데이터 표현 시 사용하는 자료형 (8바이트, 소수점 15자리) - long double은 12바이트, 소수점 18자리
else  //if~else의 그 else
enum
extern
float //실수 데이터 표현 시 사용하는 자료형 (4바이트, 소수점 6자리)
for //for loop문
goto  //
if  //if문
_Imaginary
register//변수 선언 시 추가할 수 있는 선언 (선언방식) resigter int num=0;
        //접근이 가장 빠른 레지스터에 저장하라고 컴파일러에게 요청 (빈번히 사용하는 변수의 경우에)
        //레지스터 메모리는 너무 작고 소중하기에... 계속 자리를 차지하는 전역변수에는 register 선언을 추가할 수 없다 (컴파일러 선에서 커트, 할당돼도 의미가 없다)
return  //함수의 반환값
restrict
short //정수 데이터 표현 시 사용하는 자료형 (2바이트)
signed  //"정수 자료형의 이름에 한해!" 앞에 signed 선언을 추가할 수 있다.(생략 가능) int num == signed int num. 의미는 안변한다.
        // (char은 예외일 수 있어 char형 변수에 음의 정수를 저장하는 경우에는 signed 선언을 추가하기도 함)
sizeof  //(연산자!) 소모하는 메모리의 크기를 바이트 단위로 계산하여 반환. 변수, 상수, 자료형의 이름도 올 수 있다
static  // 지역변수에 static 선언이 붙게 되면, 전역변수의 성격을 지니는 변수가 된다. (선언방식) static int num(이 경우 0으로 초기화); static int num=0;
        // (특성1) 선언된 함수 내에서만 접근이 가능.
        // (특성2) 1회만 초기화. 초기화하지 않으면 0으로 초기화. (사실상 프로그램 시작과 동시에 할당 및 초기화 돼 변수를 선언한 반복문 내에서 초기화 값으로 다시 세팅되지 않음)
        // (특성3) 프로그램 종료 시까지 메모리 공간에 존재
struct  //구조체 선언 시 사용
switch
typedef //
union //
unsigned  //"정수 자료형의 이름에 한해!" 앞에 unsigned 선언을 추가하면, 0 이상의 값만 표현하는 자료형이 된다. (MSB를 값의 크기를 나타내는 비트로 사용, +/-의 기준이 없어짐)
void  //함수의 입력값이나 반환값이 없을 때 사용
volatile
while //while loop문
