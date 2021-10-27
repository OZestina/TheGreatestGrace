//감자->삐삐, 양파->엥엥
public void myFunction() {
  //입력용 스캐너 객체 생성
  Scanner sc = new Scanner(System.in);

  System.out.print("데이터 입력>> ");
  String sentence = sc.nextLine();
  String[] words = sentence.split(" ");
  for (int i = 0; i < words.length; i++) {
    if (words[i].equals("감자")) {
      System.out.println("삐삐");
    } else {
      System.out.println("엥엥");
    } 
  }
  //스캐너 객체 close
  sc.close();
}
