package day13;

import java.util.Arrays;

public class Practice {

	public static void main(String[] args) {
		
		//원본 배열
		int[] arrInt = {1,2,3,4,5,6};
		
		//복사 배열
//		int[] arrInt2 = new int[5];
		int[] arrInt2 = null;
		
		//arrInt2를 길이 5인 배열로 선언(기본값 0), arrInt 복사
		//원본이 저장공간보다 더 크더라도 크기만큼만 복사&저장됨! 짱이다
		arrInt2 = Arrays.copyOf(arrInt, 5);
		
		//배열 값 출력
		for (int i = 0; i < arrInt2.length; i++) {
			System.out.println(arrInt2[i]);
		}
	}

}
