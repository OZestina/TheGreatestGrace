//groom
//https://level.goorm.io/exam/43111/%ED%99%80%EC%A7%9D-%ED%8C%90%EB%B3%84/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
		
		int number = Integer.parseInt(input);
		if (number%2 == 0) {
			System.out.println("even");
		} else {
			System.out.println("odd");
		}
	}
}
