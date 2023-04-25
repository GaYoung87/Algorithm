import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution_20230425_1966_프린터큐 {

    /**
     * [A,1],[B,2],[C,3],[D,4]인데 이중에 M=2=3-1=C가 몇번째로 인쇄되는지
     *
     * @param args
     */
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();

        for (int t = 0; t < T; t++) {

            int N = in.nextInt();
            int M = in.nextInt();
            Queue<int[]> q = new LinkedList<>();
            for(int i = 0; i < N; i++) {
                q.offer(new int[] {i, in.nextInt()});
            }

            int cnt = 0;
            while (!q.isEmpty()) {
                int[] first = q.poll();
                boolean isMax = true;  // 가장 높은 중요도인지 확인

                for (int x[] : q) {
                    if (x[1] > first[1]) {
                        isMax = false;
                        break;
                    }
                }

                if (isMax) {
                    cnt++;
                    if (first[0] == M) {
                        break;
                    } else {
                        q.offer(first);
                    }
                }
            }

            System.out.println(cnt);
        }
    }
}
