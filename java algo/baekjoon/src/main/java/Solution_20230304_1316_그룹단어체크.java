import java.util.Scanner;

public class Solution_20230304_1316_그룹단어체크 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int T = in.nextInt();

        int count = 0;
        for (int t=0; t<T; t++) {


            if (check(in.next())) {
                count++;
            }
        }

        System.out.println(count);

    }

    private static boolean check(String word) {

        int[] alpha = new int[26];  // 단어가 나온적이 있는지 표시
        int pre_idx = 0;
        for (int i=0; i<word.length(); i++) {
            int now_idx = word.charAt(i);

            // 앞에 문자랑 i번째 문자가 같으면
            if (pre_idx == now_idx) {
                continue;
            } else { // 앞에 문자랑 i번째 문자가 다르면
                if (alpha[now_idx - 'a'] == 0) {  // 처음 나온 문자면
                    alpha[now_idx - 'a'] = 1;
                    pre_idx = now_idx;
                } else {  // 이미 나온적 있는 문자면
                    return false;  // 그룹단어가 아님
                }
            }
        }
        return true;
    }
}
