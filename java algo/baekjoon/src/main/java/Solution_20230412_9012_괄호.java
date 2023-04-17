import java.util.Scanner;
import java.util.Stack;

public class Solution_20230412_9012_괄호 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int T = in.nextInt();

        for(int i = 0; i < T; i++) {
            System.out.println(check(in.next()));
        }
    }

    public static String check(String word) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < word.length(); i++) {

            char c = word.charAt(i);

            if (c == '(') {
                stack.push(c);
            } else if (stack.empty()) {
                // 스택이 비어있는 경우. 즉, 닫는 괄호를 입력받았으나 pop할 원소가 없을 경우
                return "NO";
            }
            // 그 외의 경우 stack 원소를 pop 한다.
            else {
                stack.pop();
            }
        }

        if (stack.empty()) {
            return "YES";
        } else {
            return "NO";
        }
    }
}
