//이중for문 이용, 구구단 찍기

public void ggd() {

  for (int i = 2; i < 10; i++) {
    System.out.println("=====[ "+i+"단 ]=====");
    for (int j = 1; j < 10; j++) {
      System.out.println(i+" x "+j+" = "+(i*j));
    }
    System.out.println();
  }
}



//구구단 3단에서 4의 배수를 제외하고 출력
public void ggd3() {
  for (int i = 2; i < 10; i++) {
    System.out.println("=====[ "+i+"단 ]=====");
    for (int j = 1; j < 10; j++) {
      if (i==3 & j%4 == 0) { continue; }
      else { System.out.println(i+" x "+j+" = "+(i*j)); }
    }
    System.out.println();
  }
}
