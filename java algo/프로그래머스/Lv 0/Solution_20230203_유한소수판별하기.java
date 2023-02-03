public class Solution_20230203_유한소수판별하기 {

    public int solution(int a, int b) {
        int answer = 2;
        // 약분하기
        for (int i=1; i<Math.min(a, b) + 1; i++) {
            if (a % i == 0 && b % i == 0) {
                a /= i;
                b /= i;
            }
        }

        // 소인수찾기
        if (check(b)) {
            answer = 1;
        }
        return answer;
    }

    // 소인수 찾기
    public boolean check(int num){
        while (num > 1) {
            if (num % 2 == 0) {
                num /= 2;
            } else if (num % 5 == 0) {
                num /= 5;
            } else {
                return false;
            }
        }
        return true;
    }
}
