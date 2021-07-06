package practice;

import java.util.Random;

public class Practice {

    public static void main(String[] args) {
        int sum = 0;
        int i = 1;

        do{
            sum += i;
            i++;
        }while(i<=100);

        System.out.println("합계: "+sum);

        int j = 10;
        do {
            System.out.println("j: "+j);
        }while(j<10);

    }
}
