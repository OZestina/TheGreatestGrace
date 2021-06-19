public class StringApp {
  
  public static void main(String[] args) {
    
    System.out.println("Hello World");  //String
    System.out.println("H");            //String
    System.out.println('H');            //Character
    
    System.out.println("Hello "
                       + "World");      //+ 는 문자열을 더해주는(이어지게 하는) 것
    
    System.out.println("Hello \nWorld");  //\n 은 줄바꿈 문자
    
    System.out.println("Hello \"World\"");  // Hello "World"
    
  }
}


public class StringOperation {
  
  public static void main(String[] args) {
    
    System.out.println("Hello World".length()); // 11 (물론 띄어쓰기도 포함!)
    System.out.println("Hello, user_name ... bye.".replace("user_name", "Zestina"));  //Hello, Zestina ... bye.
    
  }
}
