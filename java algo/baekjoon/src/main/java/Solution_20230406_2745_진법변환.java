import java.util.Scanner;

public class Solution_20230406_2745_진법변환 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int n = in.nextInt();
        /**
         * 2진수 1101 = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0
         */

        int tmp = 1;
        int ans = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);

            if ('A' <= c && c <= 'Z') {
                ans += (c - 'A' + 10) * tmp;
            } else {
                ans += (c - '0') * tmp;
            }
            tmp *= n;
        }
        System.out.println(ans);
    }
}