package practice;

import java.util.Random;

public class Practice {

    public static void main(String[] args) {

        //<<, >> 연산
        System.out.println(3<<2);   //3*2^2 = 12
        System.out.println(-12<<2);   //-12*2^2 = -48

        System.out.println(8>>2);   //8/2^2 = 2
        System.out.println(-48>>2);   //-48/2^2 = -12

        // >>> 연산: 왼쪽 비트를 0으로 채움
        System.out.println(8 >>>3); //8/2^3 = 1
        System.out.println(-8 >>>3);
        System.out.println(Integer.toBinaryString(-8));
        System.out.println(Integer.toBinaryString(-8>>>3));
    }
}
