import java.util.Scanner;

public class Solution_20230223_11720_숫자의합 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String x = in.next();

        String[] array = x.split("");
        int answer = 0;
        for (String a : array) {
            answer += Integer.parseInt(a);
        }
        System.out.println(answer);
    }
}
