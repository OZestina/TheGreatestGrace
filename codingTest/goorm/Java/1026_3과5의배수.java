//groom
//https://level.goorm.io/exam/43166/3%EA%B3%BC-5%EC%9D%98-%EB%B0%B0%EC%88%98/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
		
		int number = Integer.parseInt(input);
		int a = number/3 * (number/3 + 1) / 2;
		int b = number/5 * (number/5 + 1) / 2;
		int c = number/15 * (number/15 + 1) / 2;
		int result = a*3 + b*5 - c*15;
		
		System.out.println(result);		
		
	}
}
