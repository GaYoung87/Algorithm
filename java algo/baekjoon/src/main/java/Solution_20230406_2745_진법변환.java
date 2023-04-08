import java.util.Scanner;

public class Solution_20230406_2745_진법변환 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String word = in.next();
        int n = in.nextInt();
        /**
         * 2진수 1101 = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0
         */

        int answer = 0;
        int idx = 0;  // 몇승인지

        for (int i=word.length()-1; i>=0; i--) {
            char c = word.charAt(i);

            if ('A' <= c && c <= 'Z') {
                answer += (c - 'A' + 10) * idx;  // 10을 더하는 이유가 문제에서 A:10이기 때문
                System.out.println(answer);
            } else {  // 숫자
                System.out.println("number : " + c);
                answer += (c - '0') * idx;
                idx++;
                System.out.println(answer);
            }

        }
    }
}