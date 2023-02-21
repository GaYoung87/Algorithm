import java.util.HashMap;
import java.util.Map;

/**
 * banana이면
 * {b:0} -> {b:0, a:1} -> {b:0, a:1, n:2} -> {b:0, a:3, n:2} 이렇게 문자의 인덱스를 표시해주면서 가장 가까운 글자 찾기
 */
public class Solution_20230217_가장가까운같은글자 {

    public int[] solution(String s) {
        int[] answer = new int[s.length()];

        String[] ss = s.split("");
        Map<String, Integer> check = new HashMap<String, Integer>();
        for (int i=0; i<ss.length; i++) {
            if (check.get(ss[i]) == null) {
                answer[i] = -1;
            } else {
                answer[i] = i - check.get(ss[i]);
            }

            check.put(ss[i], i);

        }

        return answer;
    }
}
