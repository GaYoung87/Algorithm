import java.util.Arrays;

public class Solution_20230201_삼각형의완성조건2 {

    public int solution(int[] sides) {

        Arrays.sort(sides);
        int my_min = sides[0];
        int my_max = sides[1];

        int answer = 0;

        for (int i=my_max+1; i<my_max+my_min; i++) {
            answer ++;
        }

        for (int i=my_max-my_min+1; i<=my_max; i++) {
            answer ++;
        }

        return answer;
    }
}
