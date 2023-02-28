import java.util.Scanner;

public class Solution_20230227_10809_알파벳찾기 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        String word = in.nextLine();
        int[] alpha = new int[26];
        for (int i=0; i<26; i++) {
            alpha[i] = -1;
        }

        for (int j=0; j<word.length(); j++) {
            char ch = word.charAt(j);

            if (alpha[ch - 'a'] == -1) {
                alpha[ch - 'a'] = j;
            }
        }

        for (int a : alpha) {
            System.out.print(a + " ");
        }
    }
}
