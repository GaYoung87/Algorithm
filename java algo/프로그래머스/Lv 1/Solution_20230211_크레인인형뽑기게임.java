import java.util.Stack;

/**
 * 바구니 역할(array)을 해줄 stack을 준비하고, 0을 넣는다.
 *    0을 넣는 이유는 stack의 맨 위 값과 비교해야하는데 아무것도 없으면 오류가 나기 때문이다.
 * moves의 길이만큼 for문을 돌린다.
 * 해당 라인에서 인형을 뽑기 위해 board의 길이만큼 for문을 돌린다.
 * 만약 board[i][move - 1]이 0이 아니면 array(바구니)의 가장 윗 요소와 board[i][move - 1]가 같은지 비교한다.
 * 같다면 인형이 터지는 것이기 때문에 Stack에 pop을 하고 answer에 2를 더한다.
 * 다르다면 Stack에 board[j][move - 1]를 push한다.
 * answer를 리턴한다.
 */

// stack 사용방법
public class Solution_20230211_크레인인형뽑기게임 {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        // 이 문제를 처음 풀 때는 인형을 담는 바구니를 ArrayList를 통해 인형을 모두 담아
        // 연속하는 인형을 인덱스로 참조해 제거하는 방식을 사용하고자 했는데,
        // 잘 생각해보니 인형이 1,2,2,1과 같은 순으로 들어갔다면
        // 2번 인형들이 지워지고 그 자리에 1번이 내려와 또 다시 1번 인형들이 지워져야 하는 점을 만족시킬 수 없었다.
        // 그래서 Stack 사용
        Stack<Integer> array = new Stack<>();
        array.push(0);  // 처음에 비교할 때 값이 없으면 EmptyStackException 에러남

        for (int move : moves) {
            for (int i = 0; i < board.length; i++) {
                if (board[i][move-1] != 0) {
                    if (array.peek() == board[i][move-1]) {
                        array.pop();
                        answer += 2;
                    } else {
                        array.push(board[i][move-1]);
                    }
                    board[i][move-1] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}
