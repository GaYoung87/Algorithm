public class Solution_20230207_다트게임 {

    // 다트 게임은 총 3번의 기회로 구성된다.
    public int solution(String dartResult) {
        int answer = 0;
        String[] dart = dartResult.split("");
        int [] score = new int[3];
        int score_idx = -1;

        for (int i=0; i<dartResult.length(); i++) {
            // 숫자면
            if (dart[i].matches("[0-9]")) {
                //System.out.println("dart[i] = " + dart[i]);
                score_idx++;
                score[score_idx] = Integer.parseInt(dart[i]);
                // System.out.println("score[score_idx] = " + score[score_idx]);
                if (dart[i+1].matches("[0-9]")) {
                    score[score_idx] = 10;
                    i++;
                }
            }

            switch (dart[i]) {
                case "D":
                    score[score_idx] = (int)Math.pow(score[score_idx], 2);  // (int)를 안해주면 결과가 double임
                    break;
                case "T":
                    score[score_idx] = (int)Math.pow(score[score_idx], 3);
                    break;
                case "*":
                    score[score_idx] *= 2;
                    if (score_idx >= 1) {
                        score[score_idx - 1] *= 2;
                    }
                    break;
                case "#":
                    score[score_idx] *= -1;
                    break;

            }
//            System.out.println("score = " + score[score_idx]);

        }

//        System.out.println("-----------------------");
        for (int s : score) {
//            System.out.println("s = " + s);
            answer += s;
        }

        return answer;

    }


}

