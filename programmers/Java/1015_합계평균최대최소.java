//int로만 구성된 배열이 있을 때 합계, 평균, 최댓값, 최솟값 구하는 프로그램

public void myFunction(int[] numbers) {
  
  //합계 출력
  int sum = 0;
  for (int i : numbers) { sum += i; }
  System.out.println("합계: " + sum);
  
  //평균 출력
  double avg = (double)sum/numbers.length;
  System.out.println("평균: "+avg);
  
  //최댓값, 최솟값
  Arrays.sort(numbers);
  System.out.println("최댓값: "+numbers[numbers.length-1]);
  System.out.println("최솟값: "+numbers[0]);
}
