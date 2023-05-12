package Lv2;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Solution_20230512_소문 {

    public int solution(int n, int k, int[][] acquaintance) {
        int[] visit = new int[101];
        int[][] adj = new int[101][101];

        for (int i = 0; i < acquaintance.length; i++) {
            adj[acquaintance[i][0]][acquaintance[i][1]] = 1;
            adj[acquaintance[i][1]][acquaintance[i][0]] = 1;
        }

        int[] dist = new int[101];
        Arrays.fill(dist, -1);

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visit[1] = 1;
        dist[1] = 0;

        while (!queue.isEmpty()) {
            int temp = queue.poll();
            for (int next=1; next<=n; next++) {
                if (adj[temp][next] == 1 && visit[next]==0) {
                    queue.offer(next);
                    visit[next] = 1;
                    dist[next] = dist[temp] + 1;
                }
            }
        }

        return dist[k];
    }
}
