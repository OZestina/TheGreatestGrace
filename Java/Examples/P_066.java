package 문제풀이;

public class Practice {
	
	public static void main(String[] args) {
		
		//10진수를 2진수로 변환
		System.out.println("3: "+Integer.toBinaryString(3));
		
		//비트 논리 연산
		System.out.println("2&3: "+(2&3));
		System.out.println("2|3: "+(2|3));
		System.out.println("2^3: "+(2^3));
		System.out.println("~3: "+(~3));
		
		//첫자리는 부호를 나타내는 비트. ~는 부호를 포함한 모든 비트를 반대로 변환
		//0의 반대는 -1, int는 양수가 음수보다 한 수 적게 카운팅 가능
		System.out.println("~3을 이진수로: "+Integer.toBinaryString(~3));
		System.out.println("-3을 이진수로: "+Integer.toBinaryString(-3));
		System.out.println("0을 이진수로: "+Integer.toBinaryString(0));
		System.out.println("-1을 이진수로: "+Integer.toBinaryString(-1));
		
		//~3의 2진수 값의 길이
		//첫자리는 부호를 나타내는 비트. 
		//나머지 31자리로 정수 자료형을 메모리에 저장
		System.out.println(Integer.toBinaryString(~3).length()); //-4의 길이
		System.out.println(Integer.MAX_VALUE);	//정수 자료형의 최대값 (2^31 -1)
		System.out.println(Integer.parseInt("1111111111111111111111111111100",2)-Integer.MAX_VALUE-1);
		
		

	}

}
