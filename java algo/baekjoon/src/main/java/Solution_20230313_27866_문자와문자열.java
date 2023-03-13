import java.util.Scanner;

public class Solution_20230313_27866_문자와문자열 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String word = in.next();
        int n = in.nextInt();

        System.out.println(word.charAt(n-1));
    }
}
