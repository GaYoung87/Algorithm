import java.util.Scanner;

public class Solution_20230303_10988_팰린드롬인지확인하기 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String word = in.next();
        int n = word.length();

        boolean flag = true;
        for (int i=0; i<word.length()/2; i++) {
            if (word.charAt(i) != word.charAt(n-i-1)) {
                flag = false;
                System.out.println(0);
                return;
            }
        }

        System.out.println(1);

    }
}
