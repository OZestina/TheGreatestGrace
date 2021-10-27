//1~n까지의 숫자 중 3의 배수만 더해서 출력하는 프로그램
//가능한 다양한 방법 중 연산과정을 줄이기 위해 1+n/3(몫만) 의 값을 구한 후 3배를 하는 프로그램으로 진행

public void myFunction(int number) {
  //결과 계산용 변수
  int result = 0;

  int n = number/3;

  for (int i = 1; i <= n; i++) { result += i; }
  System.out.println(result * 3);
  }
}
