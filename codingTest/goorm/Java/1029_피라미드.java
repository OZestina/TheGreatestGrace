//goorm
//https://level.goorm.io/exam/43181/%ED%94%BC%EB%9D%BC%EB%AF%B8%EB%93%9C/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int floor = Integer.parseInt(br.readLine());
		// System.out.println("Hello Goorm! Your input is " + input);
		
		Main a = new Main();
		a.pyramid(floor);
		
	}
	
	public void pyramid(int floor) {
		for(int i = 0; i<floor; i++){
			for (int j = 0; j<floor-(i+1); j++){
				System.out.print(' ');
			}
			for (int j = 0; j<(2*i+1); j++){
				System.out.print('*');
			}
			System.out.println();
		}
	}
	
}
