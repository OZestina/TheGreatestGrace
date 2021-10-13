// 영문자로 이루어진 String을 입력받으면 알파벳이 각각 몇글자인지 체크하는 프로그램 만들기 
// a(2) b(3) c(2) 

public class CodingTest1013_1 {

	public static void main(String[] args) {
		
		CodingTest1013_1 test1 = new CodingTest1013_1();
		test1.alphabetCount("aabbbcc");
	}
	
	public void alphabetCount (String text) {
		
		HashMap<Character, Integer> resultArray = new HashMap<>();
		
		for (int i = 0; i < text.length(); i++) {
			if (resultArray.containsKey(text.charAt(i))) {
				resultArray.put(text.charAt(i), resultArray.get(text.charAt(i))+1);
			} else {
				resultArray.put(text.charAt(i), 1);
			}
		}
		
		for (Character c : resultArray.keySet()) {
			System.out.print(c+"("+resultArray.get(c)+") ");
		}
	}
}
