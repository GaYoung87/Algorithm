import java.util.*;

public class Solution_20230202_등수매기기_2 {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        List<Integer> score_avg = new ArrayList<>();
        // int[] score_avg = new int[score.length];

        // int로 하게되면 /2했을 때 소수점이 필요한 경우 나오지 않음 -> float로 지정하거나 평균내지않고 합으로만 진행
        for (int i=0; i<score.length; i++) {
            score_avg.add(score[i][0] + score[i][1]);
        }

        System.out.println(score_avg);

        score_avg.sort(Comparator.reverseOrder());

        for (int i=0; i<score_avg.size(); i++) {
            answer[i] = score_avg.indexOf(score[i][0] + score[i][1])+1;
        }

        return answer;
    }
}
