import java.util.Scanner;

public class Solution_20230309_1436_영화감독숌 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int num = 666;
        int count = 1;

        // count == n일 때까지 num++하고, int를 String으로 바꿔서 666포함이면 return
        while (count != n) {
            num++;

            // int를 String으로 바꿔서 666이 포함되면 count++;
            // 이때, count == n이면 해당 num 뽑기
            if (String.valueOf(num).contains("666")) {
                count++;
            }
        }

        System.out.println(num);
    }
}
