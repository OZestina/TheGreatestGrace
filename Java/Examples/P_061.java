package 복습;

public class practice {

	public static void main(String[] args) {

		int a = 10;
		int b = 5;
		
		System.out.println(a>b && a==10);	//true
		System.out.println(a>b && a==b);	//false
		
		System.out.println(a>b || a==b);	//true
		System.out.println(a<b || a==b);	//false

		System.out.println(a>b ^ a==10);	//false
		System.out.println(a>b ^ a==b);		//true
		
		System.out.println(!(a>b));			//false
		System.out.println(!(a<b));			//true
		
		
	}

}
