import java.util.ArrayList;
import java.util.Collections;

public class Solution_20230219_명예의전당1 {

    /**
     * @param k
     * @param score
     * @return
     *
     * [ 진행과정 ]
     * //1. check = int[]로 두고
     * //2. check.length < k이면 값을 넣고 > k이면 check를 돌면서 넣는다 -> 문제 발생!!!! -> [10.20.100]인데 150넣으려면 [10.20.150]으로 바꾸는게 아닌 [20,100,150]이 되어야함
     * 1. check = ArrayList<>()로 두고
     * 2. check.length < k이면 값을 넣고 최소값 찾아 answer에 넣기
     * 3. check.length = k이면 최소값 자리에 최대값을 넣고, 최소값 찾아 answer에 넣기
     */
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        ArrayList<Integer> check = new ArrayList<>();

        for (int i=0; i<score.length; i++) {
            if (check.size() < k) {
                check.add(score[i]);
                Collections.sort(check);
                answer[i] = check.get(0);

            } else if (check.size() == k) {

                int mymin = check.get(0);
                if (mymin < score[i]) {
                    check.remove(0);
                    check.add(score[i]);
                    Collections.sort(check);
                }
                answer[i] = check.get(0);
            }
        }
        return answer;
    }
}
