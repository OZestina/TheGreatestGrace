package day13;

public class Practice {

	public static void main(String[] args) {
		
		//배열
		String[] names = {"홍", "이","김"};
		int[] score = {1,2,3};
		
		//인덱스 변수 선언&초기화
		int i = 0;
		
		//foreach문
		for(String name : names) {
			System.out.println(name+": "+score[i]);
			i++;
		}
	}

}
