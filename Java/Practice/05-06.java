//내가 푼것!
//층 수 변화해도 적용되도록 함
//뒷 공간에도 빈칸 있어요

package practice;

public class Practice {

    public static void main(String[] args) {
        int floor = 5;
        for (int i = 0; i<floor; i++){
            for (int j=0;j<(floor*2-1);j++){
                if ((floor-1-i)<=j && j<(i+floor)){
                    System.out.print("*");
                } else{
                    System.out.print(" " );
                }
            }
            System.out.println();
        }

    }
}


//답지
//뒷 공간에는 빈칸 없어요
package practice;

public class Practice {

    public static void main(String[] args) {
        int floor = 5;
        for (int i = 0; i<floor; i++){
            for (int j=(floor-i); j>0; j--){
                System.out.print(" ");    //빈칸 출력
            }
            for (int k = 0; k<(i*2)+1; k++){
                System.out.print("*");    //별 출력
            }
                
            System.out.println();
        }

    }
}
