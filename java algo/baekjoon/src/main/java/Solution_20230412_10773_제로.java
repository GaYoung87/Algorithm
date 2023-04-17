import java.util.Scanner;
import java.util.Stack;

public class Solution_20230412_10773_제로 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int K = in.nextInt();
        Stack<Integer> stack = new Stack<Integer>();

        for (int i=0; i<K; i++) {
            int num = in.nextInt();

            if(num != 0) {	// stack에 원소 추가
                stack.push(num);  // add()로 대체 가능
            }else {	// 0이라면 스택에 저장된 top 원소를 지운다.
                stack.pop();
            }
        }

        int sum = 0;
        for(int s : stack) {	// 합을 구할 때 K가 아닌 top까지이다.
            sum += s;
        }

        System.out.println(sum);
    }
}
