//https://level.goorm.io/exam/49107/%EC%86%8C%ED%9D%AC%EC%99%80-%EB%B2%84%EC%8A%A4/quiz/1

import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		//버스 대수
		int buses = Integer.valueOf(input[0]);
		//소희 도착 시간
		int atTime = Integer.valueOf(input[1]);
		
		//버스 대수 길이의 배열 생성 (소희가 탈 수 있는 각 버스의 도착 시간 저장)
		int[] schedule = new int[buses];
		
		//소희가 탈 수 있는 각 버스의 도착 시간 저장
		for (int i = 0; i < buses; i++) {
			String[] input2 = br.readLine().split(" ");
			int[] busInput = {Integer.valueOf(input2[0]), Integer.valueOf(input2[1])};
			while (busInput[0] < atTime) {
				busInput[0] += busInput[1];
			}
			schedule[i] = busInput[0];
		}
		
		//버스 도착시간 중 가장 빠르고 번호가 낮은 버스 출력
		int idx = 0;
		for (int i = 1; i < buses; i++) {
			if (schedule[idx] > schedule[i]) {
				idx = i;
			}
		}
		System.out.println(idx+1);
	}
}
