public class Solution_20230121_자릿수더하기_1 {  // 자릿수 더하기_방법1

    public int solution(int n) {
        int answer = 0;
        String num = Integer.toString(n);

        for (int i=0; i<num.length(); i++) {
            answer += Integer.parseInt(num.substring(i, i+1));
        }

        return answer;
    }
}
