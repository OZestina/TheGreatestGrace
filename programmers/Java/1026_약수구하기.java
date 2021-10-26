//groom
//https://level.goorm.io/exam/43255/%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
		
		int number = Integer.parseInt(input);
		String result = "";
		
		for (int i = 1; i <= number/2; i++) {
			if (number % i == 0) {
				result += i+" ";
			}
		}
		result += number+" ";
		
		System.out.println(result);
		
	}
}
