package Lv2;

import java.util.LinkedList;
import java.util.Queue;

public class Solution_20230511_컴맹의반란 {

    public int solution(int n, int[][] connect) {

        int[] visit = new int[101];
        int[][] board = new int[101][101];
        int answer = 1;

        // board채우기
        for (int i = 0; i < connect.length; i++) {
            board[connect[i][0]][connect[i][1]] = 1;
            board[connect[i][1]][connect[i][0]] = 1;
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(1);
        visit[1] = 1;
        while (!queue.isEmpty()) {
            int temp = queue.poll();

            for (int x = 1; x<=n; x++) {
                if (board[temp][x]==1 && visit[x]==0) {
                    queue.offer(x);
                    visit[x] = 1;
                    answer++;
                }
            }

        }

        return answer;
    }
}
