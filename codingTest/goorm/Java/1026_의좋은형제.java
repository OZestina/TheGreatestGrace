//groom
//https://level.goorm.io/exam/49088/%EC%9D%98%EC%A2%8B%EC%9D%80-%ED%98%95%EC%A0%9C/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String input2 = br.readLine();
		// System.out.println("Hello Goorm! Your input is " + input);
		
		String[] food = input.split(" ");
				
		Main a = new Main();
		a.brothers(Integer.parseInt(food[0]), Integer.parseInt(food[1]), Integer.parseInt(input2));
		
	}
	
	public void brothers (int n1, int n2, int day) {
		for(int i = 0; i < day; i++) {
			if (i%2 == 0) {
				if (n1%2 == 0) { n2 += n1/2; n1 = n1/2;
				} else { n2 += n1/2 + 1; n1 -= n1/2 + 1;}
			} else {
				if (n2%2 == 0) { n1 += n2/2; n2 = n2/2;
				} else { n1 += n2/2 + 1; n2 -= n2/2 + 1; }
			}
			//System.out.println(n1+" "+n2);
		}
		System.out.println(n1+" "+n2);
	}
	
}
