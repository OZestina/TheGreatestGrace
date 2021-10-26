//groom
//https://level.goorm.io/exam/43094/%EC%8B%9C%ED%97%98%EC%84%B1%EC%A0%81-%ED%8F%89%EA%B7%A0%EA%B3%BC-%EB%93%B1%EA%B8%89-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
		
		String[] scores = input.split(" ");
		double totalScore = 0.0;
		for(int i = 0; i< scores.length; i++) {
			totalScore += Double.parseDouble(scores[i]);
		}
		int avgScore = (int) Math.round(totalScore * 100 / scores.length);
		
		String grade = avgScore/100 + "." + avgScore%100;
		if (avgScore%100==0 || avgScore%100%10 == 0) {
			grade += "0";
		}
		if (avgScore >= 9000) {
			grade += " A";
		} else if (avgScore >= 8000) {
			grade += " B";
		} else if (avgScore >= 7000) {
			grade += " C";
		} else if (avgScore >= 6000) {
			grade += " D";
		} else {
			grade += " F";
		}
		System.out.println(grade);
	}
}
