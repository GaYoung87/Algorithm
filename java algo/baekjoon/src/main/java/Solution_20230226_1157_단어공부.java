import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Solution_20230226_1157_단어공부 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String word = in.next().toLowerCase();
        int[] alpha = new int[26];

        for (int i=0; i<word.length(); i++) {
            if ('A' <= word.charAt(i) && word.charAt(i) <= 'Z') {
                alpha[word.charAt(i) - 'A']++;
            }
        }

        Arrays.sort(alpha);
        int mymax = alpha[25];


        int check = 0;
        int idx = 0;
        for (int i=0; i<26; i++) {
            if (mymax == alpha[i]) {
                check++;
            }
        }


    }
}
