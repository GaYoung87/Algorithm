public class Solution_20230218_이상한문자만들기 {

    public String solution(String s) {
        String answer = "";
        String[] ss = s.split("");

        int idx = 0;
        for (int i=0; i<ss.length; i++) {
            if (ss[i].equals(" ")) {
                idx = 0;
            } else if(idx % 2 == 0) {
                ss[i] = ss[i].toUpperCase();
                idx++;
            } else {
                ss[i] = ss[i].toLowerCase();
                idx++;
            }
            answer += ss[i];
        }
            return answer;
    }
}
