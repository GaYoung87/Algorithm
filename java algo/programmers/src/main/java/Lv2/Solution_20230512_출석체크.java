package Lv2;

import java.util.*;

public class Solution_20230512_출석체크 {

    public String[] solution(String[] names) {
        String[] answer = new String[100];
        Arrays.sort(names);
        answer[0] = names[0];

        int idx = 1;
        for (int i=1; i< names.length; i++) {
            if (!names[i].equals(names[i-1])) {
                answer[idx] = names[i];
                idx++;
            }
        }

        return Arrays.copyOf(answer, idx);
    }
}
