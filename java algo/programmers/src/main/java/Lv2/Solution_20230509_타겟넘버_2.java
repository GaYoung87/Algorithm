package Lv2;

import java.util.LinkedList;
import java.util.Queue;

public class Solution_20230509_타겟넘버_2 {
    Queue<Integer> queue = new LinkedList<Integer>();

    public int solution(int[] numbers, int target) {

        int answer = 0;
        queue.offer(0);
        queue.offer(0);
        while(queue.peek() != null) {
            int level =queue.poll();
            int v = queue.poll();
            if(level==numbers.length){
                if(v==target)
                    answer++;
            }else {
                queue.offer(level + 1);
                queue.offer(v + numbers[level]);

                queue.offer(level + 1);
                queue.offer(v - numbers[level]);
            }
        }
        return 0;
    }
}
