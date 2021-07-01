package practice;

public class practice2 {

	public static void main(String[] args) {

		// 1~100까지 정수 중 5의 배수만 출력하는 프로그램
		// 조건에 맞는 정수 합계연산 처리 코드 추가

		int sum = 0; // 배수의 합을 위한 변수

		System.out.print("5의 배수: ");
		for (int i = 1; i <= 100; i++) {
			if (i % 5 == 0) {
				System.out.print(i + " "); // 5의 배수 출력
				sum += i; // 5의 배수 합계
			}
		}
		System.out.println();

		System.out.println("5의 배수의 합계는 " + sum);

		sum =0; //초기화
		for (int i = 5; i <= 100; i += 5) {
			sum += i; // 5의 배수 합계
		}

	}

}
