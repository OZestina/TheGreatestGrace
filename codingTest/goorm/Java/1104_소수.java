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
