//내가 푼것
//그러네... 게임이랑 게임 엔딩(결과 출력)이랑 구분하는게 더 낫겠네...

package practice;

import java.util.Random;

public class Practice {

    public static void main(String[] args) {
        int count = 0;  //주사위 굴린 수 카운트용
        Random r = new Random();
        int num;

        while (true){
            num = r.nextInt(6)+1;
            System.out.println("("+num+")");
            count++;
            if (num==6) {
                System.out.println("총 주사위 굴린 횟수는 : "+count);
                break;
            }
        }

    }
}


//답지

package practice;

import java.util.Random;

public class Practice {

    public static void main(String[] args) {
        int count = 0;  //주사위 굴린 수 카운트용
        while(true){
            int dice = (int)(Math.random()*6+1); //1~6 랜덤넘버 발생
            System.out.println("("+dice+")");
            count++;

            if (dice==6){
                break;
            }
        }
        System.out.println("총 주사위 굴린 횟수는: "+ count);
    }
}
