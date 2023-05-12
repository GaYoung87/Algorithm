package Lv2;

public class Solution_20230512_발렌타인데이 {

    public int solution(String[] dates) {
        int answer = 0;

        for (int i=0; i< dates.length; i++) {
            boolean flag = true;
            for (int j=0; j<dates[i].length(); j++) {
                if (dates[i].charAt(j) == '/') {
                    continue;
                } else if (dates[i].charAt(j) != '1' && dates[i].charAt(j) != '2' &&
                           dates[i].charAt(j) != '4' && dates[i].charAt(j) != '8' ) {
                    flag = false;
                }
            }

            if (flag) {
                answer++;
            }
        }
        return answer;
    }
}
