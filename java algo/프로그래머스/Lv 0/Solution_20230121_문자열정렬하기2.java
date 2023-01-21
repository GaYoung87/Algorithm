import java.util.Arrays;

public class Solution_20230121_문자열정렬하기2 {

    public String solution(String my_string) {
        String answer = "";

        String[] array = my_string.toLowerCase().split("");
        Arrays.sort(array);

        for (int i=0; i<array.length; i++) {
            answer += array[i];
        }
        return answer;
    }
}
