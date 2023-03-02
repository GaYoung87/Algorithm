import java.util.Scanner;

public class Solution_20230302_10811_바구니뒤집기 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        // 기본 배열 설정
        int[] array = new int[N];
        for (int n=0; n<N; n++) {
            array[n] = n+1;
        }

        for (int m=0; m<M; m++) {
            int a = sc.nextInt()-1;
            int b = sc.nextInt()-1;

            while (a < b) {
                int temp = array[a];
                array[a++] = array[b];  // array[b]로 변경후에 다음 값으로 넘어가야하니까
                array[b--] = temp;
            }
        }
        
        for (int i=0; i<N; i++) {
            System.out.println(array[i]);
        }
    }
}
