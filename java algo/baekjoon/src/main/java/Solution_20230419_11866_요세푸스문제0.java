import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution_20230419_11866_요세푸스문제0 {

    /**
     * 7 3
     * 1 2 3 4 5 6 7
     * 2 3 4 5 6 7 1
     * 3 4 5 6 7 1 2 -> 3
     * -----------------------
     * 4 5 6 7 1 2
     * 5 6 7 1 2 4
     * 6 7 1 2 4 5 -> 6
     * -----------------------
     * 7 1 2 4 5
     * 1 2 4 5 7
     * 2 4 5 7 1 -> 2
     * -----------------------
     * 4 5 7 1
     * 5 7 1 4
     * 7 1 4 5 -> 7
     * -----------------------
     * 1 4 5
     * 4 5 1
     * 5 1 4 -> 5
     * -----------------------
     * 1 4
     * 4 1
     * 1 4 -> 1
     * -----------------------
     * 4
     * 4
     * 4 -> 4
     * -----------------------
     */
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int K = in.nextInt();

        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i <= N; i++) {
            q.add(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append('<');

        while (q.size() > 1) {

            for (int x=0; x < K-1; x++) {
                q.offer(q.poll());
            }

            sb.append(q.poll()).append(", ");
        }

        sb.append(q.poll()).append(">");
        System.out.println(sb);

    }
}
