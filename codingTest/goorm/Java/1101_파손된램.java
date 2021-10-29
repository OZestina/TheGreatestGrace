//goorm
//https://level.goorm.io/exam/49074/%ED%8C%8C%EC%86%90%EB%90%9C-%EB%9E%A8/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count = Integer.valueOf(br.readLine());
		String[] rams = br.readLine().split(" ");
		//System.out.println("Hello Goorm! Your input is " + input);
		String broken = "";
		int brokenCount = 0;
		
		Main a = new Main();
		for(int i = 0; i<count; i++) {
			if ( a.twice(Integer.valueOf(rams[i])) == false ) {
				broken += (i+1)+" ";
				brokenCount += 1;
			}
		}
		
		System.out.println(brokenCount);
		System.out.println(broken);
		
	}
	
	public boolean twice (int n) {
		if (n == 128) { return true; }
		else if ( n < 128) {	return false; }
		else if ( n	% 2 == 0 ) {	return twice(n/2); }
		else { return false; }
	}
  
}
