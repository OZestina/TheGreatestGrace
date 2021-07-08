package day13;

import java.util.Arrays;

public class Practice {

	public static void main(String[] args) {
		
		//배열
		int[] arrInt = {1,2,3,4,5};
		
		//for문
		for(int i = 0; i<arrInt.length; i++) {
			System.out.print(arrInt[i]+" ");
		}
		System.out.println();
		
		//foreach문
		for(int x : arrInt) {
			System.out.print(x+" ");
		}
	}

}
