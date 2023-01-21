public class Solution_20230118 {  // 세균 증식

    public int solution(int n, int t) {

        int answer = n;
        for (int i = 0; i < t; i++) {
            answer *= 2;
        }
        return answer;
    }
}
