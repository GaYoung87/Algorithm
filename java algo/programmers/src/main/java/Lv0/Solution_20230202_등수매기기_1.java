public class Solution_20230202_등수매기기_1 {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        // List<Integer> score_avg = new ArrayList<>();
        int[] score_avg = new int[score.length];

        // int로 하게되면 /2했을 때 소수점이 필요한 경우 나오지 않음 -> float로 지정하거나 평균내지않고 합으로만 진행
        for (int i=0; i<score.length; i++) {
            score_avg[i] = score[i][0] + score[i][1];
        }

        System.out.println(score_avg);

        for (int i=0; i<score_avg.length; i++) {
            int idx = 1;
            for (int j=0; j<score_avg.length; j++) {
                if (score_avg[i] < score_avg[j]) {
                    idx++;
                }
            }

            answer[i] = idx;
        }

        return answer;
    }
}
