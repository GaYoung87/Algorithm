import java.util.Scanner;

public class Solution_20230311_10815_숫자카드_시간초과 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] get_arr = new int[n];
        for (int i=0; i<n; i++) {
            get_arr[i] = in.nextInt();
        }

        int m = in.nextInt();
        int[] num_card = new int[m];
        for (int i=0; i<m; i++) {
            num_card[i] = in.nextInt();
        }

        for (int i = 0; i<m; i++) {  // num에 대해서 가지고있는 숫자(n) 확인하기
            boolean flag = false;
            for (int j=0; j<n; j++) {
                if (num_card[i] == get_arr[j]) {
                    flag = true;
                    break;
                }
            }

            if (flag) {
                System.out.print(1 + " ");
            } else {
                System.out.print(0 + " ");
            }
        }
    }
}
