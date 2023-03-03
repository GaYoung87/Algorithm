import java.util.Scanner;

public class Solution_20230303_4344_평균은넘겠지 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for (int i=0; i<T; i++) {

            int temp = 0;
            int x = in.nextInt();
            int[] array = new int[x];

            for (int j=0; j<x; j++) {
                int val = in.nextInt();
                array[j] = val;
                temp += val;
            }

            double mean = (temp / x) ;  // 평균
            double count = 0; // 평균 넘는 학생 수 변수

            // 평균 넘는 학생 비율 찾기
            for(int j = 0 ; j < x ; j++) {
                if(array[j] > mean) {
                    count++;
                }
            }

            System.out.printf("%.3f%%\n",(count/x)*100);
        }
    }
}
