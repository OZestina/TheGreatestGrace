//https://level.goorm.io/exam/49095/%EA%B3%A0%EC%9E%A5%EB%82%9C-%EC%BB%B4%ED%93%A8%ED%84%B0/quiz/1


import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		String[] enterNum = br.readLine().split(" ");
		
		int count = 1;
		for (int i = 1; i<Integer.valueOf(input[0]); i++) {
			if (Integer.valueOf(enterNum[i]) - Integer.valueOf(enterNum[i-1]) > Integer.valueOf(input[1])) {
				count = 1;
			} else {
				count += 1;
			}
		}
		
		System.out.println(count);
		
	}
}

//Integer.valueOf를 계속 연산할 필요 없이, int 배열로 미리 만들면 좋겠다
