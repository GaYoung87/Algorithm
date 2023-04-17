import java.util.Scanner;

public class Solution_20230412_10828_스택 {

    public static int[] stack;
    public static int size_idx = 0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        stack = new int[n];
        StringBuilder sb = new StringBuilder(); // 긴 문자열 더하는 상황에 StringBuilder 사용하기 -> 속도 빠름

        for (int i=0; i<n; i++) {
            String word = in.next();

            switch (word) {
                case "push":
                    push(in.nextInt());
                    break;

                case "pop":
                    sb.append(pop()).append('\n');
                    break;

                case "size":
                    sb.append(size()).append('\n');
                    break;

                case "empty":
                    sb.append(empty()).append('\n');
                    break;

                case "top":
                    sb.append(top()).append('\n');
                    break;

            }
        }
        System.out.println(sb);
    }

    public static void push(int num) {
        stack[size_idx] = num;
        size_idx++;
    }

    public static int pop() {
        if(size_idx == 0) {
            return -1;
        } else {
            int temp = stack[size_idx - 1];
            stack[size_idx - 1] = 0;
            size_idx--;
            return temp;
        }
    }

    public static int size() {
        return size_idx;
    }

    public static int empty() {
        if(size_idx == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    public static int top() {
        if(size_idx == 0) {
            return -1;
        } else {
            return stack[size_idx - 1];
        }
    }
}
