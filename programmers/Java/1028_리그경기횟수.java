//goorm
//https://level.goorm.io/exam/43092/%EB%A6%AC%EA%B7%B8-%EA%B2%BD%EA%B8%B0-%ED%9A%9F%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
		
		Main a = new Main();
		int result = a.league(input);
		System.out.println(result);
	}
	
	public int league(String input) {
		int participants = Integer.parseInt(input);
		int count = participants * (participants-1) / 2;
		return count;
	}
		
}
