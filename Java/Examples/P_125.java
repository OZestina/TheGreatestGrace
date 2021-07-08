package day13;


public class Practice {

	public static void main(String[] args) {
		
		//원본 배열
		int[] arrInt = {1,2,3};
		
		//복사 배열
		int[] arrInt2 = new int[5];
		
		//복사
    //System.arraycopy(원본,복사시작idx(원본),저장배열,저장시작idx(저장배열),복사할길이)
		System.arraycopy(arrInt, 0, arrInt2, 2, arrInt.length);
		
		//배열 값 출력
		for (int i = 0; i < arrInt2.length; i++) {
			System.out.println(arrInt2[i]);
		}
	}

}
