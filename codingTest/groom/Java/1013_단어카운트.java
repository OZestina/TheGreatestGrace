// 스트링을 입력받아 각 단어가 몇 번 나왔는지 프린트 
public class CodingTest {

	public static void main(String[] args) {
		
		// 스트링을 입력받아 "사람" 단어가 몇 번 나왔는지 프린트 
		CodingTest1013_1 test1 = new CodingTest1013_1();
		test1.wordCount("나는 사람, 너도 사람, 우리도 사람, 모두다 사람");
	}
	
	public void wordCount (String text) {
		//카운트용 배열 선언
		String[] words = {"사람","나는","너도","우리도","모두다"};
		int[] count = new int[5];
		//단어 개수 카운트
		for (int i = 0; i < words.length; i++) {
			int index = 0;
			while(index != -1) {
				int result = text.indexOf(words[i], index);
				if (result == -1) {
					break;
				} else {
					count[i]++;
					index = result+1;
				}
			}
		}
		//결과 출력
		System.out.print("결과: ");
		for (int i = 0; i < words.length; i++) {
			System.out.print(words[i]+"("+count[i]+") ");
		}
	}
}
