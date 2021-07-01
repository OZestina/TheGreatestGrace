package practice;

public class practice2 {

	public static void main(String[] args) {

		//1~100의 수 중 짝수와 홀수의 합 각각 구하기
		int evenSum = 0;
		int oddSum = 0;
		
		for (int i = 1; i <= 100; i++) {
			if (i%2==0) {
				evenSum += i;
			} else {
				oddSum = oddSum + i;
			}
		}
		
		System.out.println("짝수의 합계는 "+evenSum);
		System.out.println("홀수의 합계는 "+oddSum);
		
	}

}
