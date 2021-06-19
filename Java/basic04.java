public class Variable {
  
  public static void main(String[] ars) {
    
    int a = 1;  //Number->integer
    System.out.println(a);
    
    double b = 1.1; //real number -> double
    System.out.println(b);
    
    String c = "Hello World";
    System.out.println(c);
    
  }
}



public class Letter {
  
  public static void main(String[] args) {
    String name = "egoing";
    System.out.println("Hello, " + name+". Nice to meet you. Hope to see you again soon, " + name + ". Bye.");
    
    double VAT = 10.0;
    System.out.println(VAT);
  }
}



public class Casting {
  
  public static void main(String[] args) {
    
    double a = 1.1;
    double b = 1; //System.out.println(b) => 1.0
                  //double b2 = (double) 1;
    
    //int c = 1.1;  //error(double형을 int형에 저장할 수 없다)
    double d = 1.1;
    int e = (int) 1.1;  //System.out.println(e) => 1;
    
    // 1 to String
    String f = Integer.toString(1);
    System.out.println(f);            //1 (String형 1)
    System.out.println(f.getClass()); //class java.lang.String (타입 프린트해줌)
    
  }
}
