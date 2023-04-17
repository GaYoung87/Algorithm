import java.util.Scanner;
import java.util.Stack;

public class Solution_20230412_4949_균형잡힌세상 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        String s;
        while(true) {
            s = in.nextLine();

            if (s.equals(".")) {
                break;
            }
            System.out.println(check(s));
        }
    }

    public static String check(String word) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < word.length(); i++) {

            char c = word.charAt(i);

            if (c == '(' || c == '[' ) {
                stack.push(c);
            } else if (c == ')') {
                // stack.peek() = stack[top]
                // 스택이 비어있거나 stack의 마지막 값이 '('이 아닌 경우
                if (stack.empty() || stack.peek() != '(') {
                    return "no";
                } else {
                    stack.pop();
                }
            } else if (c == ']') {// ']'의 경우( ')'와 동일 )
                // stack.peek() = stack[top]
                // 스택이 비어있거나 stack의 마지막 값이 '['이 아닌 경우
                if (stack.empty() || stack.peek() != '[') {
                    return "no";
                } else {
                    stack.pop();
                }
            }
        }

        if (stack.empty()) {
            return "yes";
        } else {
            return "no";
        }
    }
}
