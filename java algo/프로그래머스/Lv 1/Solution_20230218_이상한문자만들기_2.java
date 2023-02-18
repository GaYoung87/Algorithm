public class Solution_20230218_이상한문자만들기_2 {

    public String solution(String s) {
        String answer = "";
        String[] ss = s.split("");

        int cnt = 0;
        for (String word : ss) {
            cnt = word.contains(" ") ? 0 : cnt+1;
            answer += cnt % 2 == 0 ? word.toLowerCase() : word.toUpperCase();
        }
        return answer;
    }
}
