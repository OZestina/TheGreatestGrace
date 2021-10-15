//어떤 수를 입력받아 팩토리얼을 구현한 메소드를 작성하시오

public void myFunction() {
  //입력용 스캐너 객체 생성
  Scanner sc = new Scanner(System.in);
  //수 입력받기
  System.out.print("팩토리얼을 구할 수 입력>> ");
  int number = sc.nextInt();
  int result = number;
  //팩토리얼 계산
  for (int i = 1; i < number; i++) {
    result *= i;
  }
  //출력
  System.out.println(result);
  //스캐너 객체 close
  sc.close();
}
