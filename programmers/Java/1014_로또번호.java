//1~45 사이의 랜덤 넘버를 6개를 추출하는 프로그램

public void lotto() {
  //랜덤넘버를 저장할 배열 설정: 중복값을 받지 않기 위해 set 사용
  HashSet<Integer> array = new HashSet<Integer>();

  while(array.size() < 6) {
    //1~45 사이의 랜덤 넘버 추출
    int number = (int)Math.floor(Math.random()*45+1);
    array.add(number);
  }
  
  //배열 출력
  System.out.println(array);
}
