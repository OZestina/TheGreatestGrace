package day13;

public class Practice {

	public static void main(String[] args) {
		
		String name1 = "Hong";
		String name2 = "Hong";
		String name3 = new String("Hong");
		
		System.out.println(name1);
		System.out.println(name2);
		System.out.println(name3);
		System.out.println("---------------------");
		System.out.println(name1==name2);
		System.out.println(name1==name3);
		System.out.println("---------------------");
		System.out.println(name1.equals(name2));
		System.out.println(name1.equals(name3));
		
	}

}
