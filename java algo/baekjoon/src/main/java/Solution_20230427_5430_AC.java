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

            StringBuilder sb = new StringBuilder("[");
            // RDD -> ['R','D','D']
            for (char w : word.toCharArray()) {

                // 기본 : 1, 2, 3, 4
                // 1, 2, 3, 4 + reverse=false -> 앞에값 빼기
                // 1, 2, 3, 4 + reverse=true -> 뒤에값 빼기
                boolean reverse = false;
                if (w == 'R') {
                    reverse = !reverse;

                } else {  // D
                    if (dq.isEmpty()) {
                        System.out.println("error");
                        break;
                    } else {
                        if (reverse) {
                            dq.pollLast();
                        } else {
                            dq.pollFirst();
                        }
                    }
                }


                while (!dq.isEmpty()) {
                    if (reverse) {
                        sb.append(dq.removeLast());
                    } else {
                        sb.append(dq.removeFirst());
                    }

                    if (dq.size() != 0) {
                        sb.append(',');
                    }
                }
                sb.append(']');

            }
            System.out.println(sb);
        }

    }
}
