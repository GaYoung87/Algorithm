import java.util.Scanner;

public class Solution_20230311_2839_설탕배달 {

    public static void main(String[] args) {

        /**
         * 상근이가 배달하는 봉지가 최소가 되려면 5kg짜리를 최대한으로 만들고, 나머지를 3kg으로 채워야함
         * 5로 나눠지면 바로 출력
         * 5로 안나눠지면 3을 빼면서 5로 나눠보기
         * n < 0인데도 안되면 -1 출력
         */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int count = 0;

        while (true) {
            if (n % 5 == 0) {
                count += n / 5;
                System.out.println(count);
                break;
            } else if (n < 0) {
                System.out.println(-1);
                break;
            }

            n -= 3;
            count++;

        }
    }
}
