import java.util.ArrayDeque;
import java.util.Scanner;

/**
 * 4
 * RDD
 * 4
 * [1,2,3,4]
 * DD
 * 1
 * [42]
 * RRD
 * 6
 * [1,1,2,3,5,8]
 * D
 * 0
 * []
 */
public class Solution_20230427_5430_AC {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // deque를 ArrayDeque가 아닌 LinkedList로 표현가능
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        int T = in.nextInt();

        for (int i=0; i<T; i++) {
            String word = in.next();
            int n = in.nextInt();
            String stringArr = in.next();
            for (String s : stringArr.substring(1, stringArr.length()-1).split(",")) {
                if (!s.equals("")) {
                    dq.offer(Integer.valueOf(s));
                }
            }

            // RDD -> ['R','D','D']
            for (char w : word.toCharArray()) {
                if (w == 'R') {

                }
            }


        }

    }
}
