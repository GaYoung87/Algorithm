import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Scanner;

public class Solution_20230425_1021_회전하는큐 {

    /**
     * 2, 3을 최소로 사용해서 원하는 숫자 뽑기
     * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [1]
     * [2, 3, 4, 5, 6, 7, 8, 9, 10] -> [1, 2]
     * [3, 4, 5, 6, 7, 8, 9, 10] -> [1, 2, 3]
     * answer = 0
     * -------------------------------------------
     * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> cnt = 1
     * [2, 3, 4, 5, 6, 7, 8, 9, 10, 1] -> [2]
     * [3, 4, 5, 6, 7, 8, 9, 10, 1]
     * [1, 3, 4, 5, 6, 7, 8, 9, 10] -> cnt = 2
     * [10, 1, 3, 4, 5, 6, 7, 8, 9] -> cnt = 3
     * [9, 10, 1, 3, 4, 5, 6, 7, 8] -> cnt = 4
     * [10, 1, 3, 4, 5, 6, 7, 8]
     * ...
     * [5, 6, 7, 8, 10, 1, 3, 4] -> cnt += 4
     * -------------------------------------------
     *
     * [ 풀이방법 ]
     * 중앙을 기준으로 맨 앞이 더 가깝게 2또는 3을 선택
     * deque에서 index를 찾고싶으면 LinkedList 사용해라
     */

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // deque를 ArrayDeque가 아닌 LinkedList로 표현가능
        LinkedList<Integer> dq = new LinkedList<>();
        int cnt = 0;

        int N = in.nextInt();	// 큐의 크기
        int M = in.nextInt();	// 뽑으려는 숫자의 개수

        for(int i = 1; i <= N; i++) {
            dq.offer(i);
        }

        int[] array = new int[M];	// 뽑고싶은 숫자 배열

        for(int i = 0; i < M; i++) {
            array[i] = in.nextInt();
        }

        for (int m=0; m < M; m++) {
            int target_num_idx = dq.indexOf(array[m]);
            int mid_idx;

            if(dq.size() % 2 == 0) {
                mid_idx = dq.size() / 2 - 1;
            }
            else {
                mid_idx = dq.size() / 2;
            }

            if(target_num_idx <= mid_idx) {  // 중간보다 앞이면 2번
                for (int x =0; x < target_num_idx; x++) {
                    dq.offerLast(dq.pollFirst());
                    cnt++;
                }
            } else {
                for (int x =0; x < dq.size()-target_num_idx; x++) {
                    dq.offerFirst(dq.pollLast());
                    cnt++;
                }
            }

            dq.pollFirst();
        }
        System.out.println(cnt);
    }
}