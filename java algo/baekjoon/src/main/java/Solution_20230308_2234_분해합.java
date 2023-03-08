import java.util.Scanner;

public class Solution_20230308_2234_분해합 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        /**
         N의 가장 작은 생성자를 구해야함
         그러면 1부터 N까지 다 돌면서(i) 분해합 만들기
         1. 3자리라고하면 각 자리값 수 더하면서, 몇자리숫자인지 구하기
         2. i+ 각자리숫자합 = 분해합이라면 break;


         */
        int answer = 0;
        for (int i=0; i<n; i++) {
            int sum = 0;
            int number = i;  // 198

            while (number != 0) {
                sum += number % 10;  // 8 9 1
                number /= 10;        // 19 1
            }

            if (sum + i == n) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
    }
}
