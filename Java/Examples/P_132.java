package practice;

import java.util.Arrays;

public class Practice {

    public static void main(String[] args) {

        int[] arr1 = {1,2,3};
        int[] arr2 = Arrays.copyOf(arr1,4);

        System.out.println(arr1);
        System.out.println(arr2);

        for (int i = 0; i < arr2.length; i++) {
            System.out.println(arr2[i]);
        }

    }
}
