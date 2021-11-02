//https://level.goorm.io/exam/49086/%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int square = Integer.valueOf(input);
		
		long result = 0L;
		for (long i = 1; i < square+1; i++) {
			result += i*i;
		}
		System.out.println(result);
	}
	
}
