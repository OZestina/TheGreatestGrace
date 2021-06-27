package practice;

public class Practice {

    public static void main(String[] args){

        char a = 'A';
        System.out.println("a: "+a);    //a: A

        int b = a;
        System.out.println("b: "+b);    //b: 65 (b가 int형이어서 숫자로 print)

        char c = 66;
        System.out.println("c: "+c);    //c: B

        int d = a+b;
        System.out.println("d: "+d);    //d: 130

    }
}
