public class Solution_20230205_저주의숫자3 {

    public int solution(int n) {
        int answer = 0;
        for (int i=0; i<n; i++) {
            answer++;
            while ((answer % 3 == 0) || String.valueOf(answer).contains("3")) {  // 3의 배수거나 3이 들어가면 그 다음숫자로 보내기
                    answer++;
                }
            }

        return answer;
    }
}
