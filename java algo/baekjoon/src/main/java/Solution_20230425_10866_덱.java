import java.util.ArrayDeque;
import java.util.Scanner;

public class Solution_20230425_10866_덱 {

    static ArrayDeque<Integer> dq;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        dq = new ArrayDeque<>();

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            String word = in.next();

            switch (word) {
                case "push_front":
                    push_front(in.nextInt());
                    break;

                case "push_back":
                    push_back(in.nextInt());
                    break;

                case "pop_front":
                    if (dq.isEmpty()) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(pop_front()).append('\n');
                    }
                    break;

                case "pop_back":
                    if (dq.isEmpty()) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(pop_back()).append('\n');
                    }
                    break;

                case "size":
                    sb.append(size()).append('\n');
                    break;

                case "empty":
                    sb.append(empty()).append('\n');
                    break;

                case "front":
                    if (dq.isEmpty()) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(front()).append('\n');
                    }
                    break;

                case "back":
                    if (dq.isEmpty()) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(back()).append('\n');
                    }
                    break;
            }
        }
        System.out.println(sb);

    }

    public static void push_front(int num) {
        dq.offerFirst(num);
    }

    public static void push_back(int num) {
        dq.offerLast(num);
    }

    public static int pop_front() {
        return dq.pollFirst();
    }

    public static int pop_back() {
        return dq.pollLast();
    }

    public static int size() {
        return dq.size();
    }

    public static int empty() {
        if (dq.isEmpty()) {
            return 1;
        } else {
            return 0;
        }
    }

    public static int front() {
        return dq.getFirst();
    }

    public static int back() {
        return dq.getLast();
    }
}
