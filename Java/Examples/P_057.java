package 복습;

public class practice {
	
	public static void main(String[] args) {

		int a = 10;
		int b = ++a;
		System.out.println("전위연산 결과: "+b);
		
		int x = 10;
		int y = x++;
		System.out.println("후위연산 결과: "+y);
		System.out.println("x: "+x);
		
	}

}
