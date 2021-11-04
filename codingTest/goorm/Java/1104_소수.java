//https://level.goorm.io/exam/43238/%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		
		//input값 int로 변환
		int number = Integer.valueOf(input);
		//결과값 저장 변수 생성
		String result = "True";
		//소수 여부 확인
		for(int i = 2; i <= Math.sqrt(Double.valueOf(number)); i++) {
			if (number % i == 0) {
				result = "False";
				break;
			}
		}
		//결과 출력
		System.out.println(result);
	}
}


// 1은 소수가 아니어서 False로 리턴
// 2의 배수는 추가로 계산할 필요가 없어서 i = 3 부터 홀수만 for문 진행 (연산과정 1/2로 줄어듦)

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		
		//input값 int로 변환
		int number = Integer.valueOf(input);
		
		//결과 출력
		System.out.println(isPrime(number));
	}
	public static String isPrime(int n) {
		//소수 여부 확인
		if (n == 1) { return "False"; }
		else if (n == 2) { return "True"; }
		else if (n % 2 == 0) { return "False"; }
		for(int i = 3; i <= Math.sqrt(Double.valueOf(n)); i += 2) {
			if (n % i == 0) { return "False"; }
		}
		return "True";
	}
}
