package practice;

import java.util.Arrays;

public class Practice {

    public static void main(String[] args) {

       int[] num1 = {1,2,3,4,5,6,7,8,9,10};
       int[] num2 = new int[10];

        for (int i = 0; i < num2.length; i++) {
            num2[i] = num1[i]*num1[i];
        }

        for (int i = 0; i < num2.length; i++) {
            System.out.println(num2[i]);
        }

    }
}
