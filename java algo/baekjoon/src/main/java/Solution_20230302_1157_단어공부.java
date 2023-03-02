import java.util.Scanner;

public class Solution_20230302_1157_단어공부 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String word = sc.next().toUpperCase();
        int[] alpha = new int[26];

        // 해당 문자가 나오는 갯수를 넣어주기
        for (int i=0; i<word.length(); i++) {
            if ('A' <= word.charAt(i) && word.charAt(i) <= 'Z') {
                alpha[word.charAt(i) - 'A']++;
            }
        }

        // alpha은 처음에 0으로 깔았으니까 -1로 두어 최댓값 찾기
        int mymax = -1;
        char x = '?';
        for (int i=0; i<alpha.length; i++) {
            if (alpha[i] > mymax) {
                mymax = alpha[i];
                x = (char) (i+65);  // 1+'A' => 1+65 => 66, 66은 'B'에 해당
            }
        }

        // 그 최대값을 가진 열이 2개이상이라면 '?', 하나면 해당 x출력
        int answer = 0;
        for (int i=0; i<alpha.length; i++) {
            if (alpha[i] == mymax) {
                answer++;
            }
        }

        if (answer >= 2) {
            System.out.println('?');
        } else {
            System.out.println(x);
        }

    }
}
