public class Solution_20230121_자릿수더하기_2 {  // 자릿수 더하기_방법1

    public int solution(int n) {
        int answer = 0;

        while(n > 0) {
            answer += n%10;
            n /= 10;
        }

        return answer;
    }
}
