package Lv2;

import java.util.Arrays;

public class Solution_20230511_행멘 {

    public String[] main(String word, String[] question) {
        String[] answer = {};
        boolean[] alpha = new boolean[26];
        int cnt = 0;

        // 사용되는 알파벳 알기
        for (int i=0; i<word.length(); i++) {
            if (!alpha[word.charAt(i) - 'a']) {
                alpha[word.charAt(i) - 'a'] = true;
                cnt++;
            }
        }

        // 정답맞힌 갯수
        int correct = 0; //정답 맞힌 개수
        for (int i = 0; i < question.length; i++) {
            if (alpha[question[i].charAt(0) - 'a']) {
                correct++;
                answer = Arrays.copyOf(answer, answer.length + 1);
                answer[answer.length - 1] = "\"Yes\"";
            }
            else {
                answer = Arrays.copyOf(answer, answer.length + 1);
                answer[answer.length - 1] = "\"No\"";
            }

            if (cnt == correct) {
                answer = Arrays.copyOf(answer, answer.length + 1);
                answer[answer.length - 1] = "\"SUCCESS\"";
                return answer;
            }
        }

        answer = Arrays.copyOf(answer, answer.length + 1);
        answer[answer.length - 1] = "\"FAIL\"";

        return answer;
    }
}
