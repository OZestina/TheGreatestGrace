package 문제풀이;

public class Practice {
	
	public static boolean test() {
		System.out.println("test() 메서드 실행됨");
		return true;
	}

	public static void main(String[] args) {
		
		int a = 10;
		int b = 5;
		
		//&연산
		System.out.println(a==b & test());
		
		//&&연산 - shortcut 연산 (앞 연산이 조건에 부합하지 않으면 뒷 연산 진행 노노)
		System.out.println(a==b && test());

	}

}
