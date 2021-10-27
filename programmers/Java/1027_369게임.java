//goorm
//https://level.goorm.io/exam/48757/369-%EA%B2%8C%EC%9E%84/quiz/1

import java.io.*;

class Main {
	public static void main(String[] args) throws Exception {
    
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
		
		Main a = new Main();
		int result = a.count369(input);
		System.out.println(result);
	}
	
	public int count369(String inputNum) {
		int number = Integer.parseInt(inputNum);
		
		//var for count of 3,6,9
		int count = 0;
		
		for(int i = 0; i<number; i++) {
			//숫자 스트링으로 변환
			String shout = Integer.toString(i);
			//3,6,9를 빈칸으로 치환
			String shout2 = shout.replace("3","").replace("6","").replace("9","");
			//원래 스트링 길이와 치환한 스트링 길이 비교하여 count 증가
			count += shout.length() - shout2.length();
		}
		return count;
	}
	
}
