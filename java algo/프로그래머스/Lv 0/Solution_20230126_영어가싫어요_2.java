import java.util.ArrayList;
import java.util.List;

public class Solution_20230126_영어가싫어요_2 {

    public long solution(String numbers) {
        long answer = 0;
        String[] number = numbers.split("");  // onetwonine -> o n e t w o n i n e
        ArrayList<String> ls = new ArrayList<>();  // 문자로 지정해야 129로 붙는다

        String[] str = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        long[] num = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

        String string = "";
        for (int i = 0; i < number.length; i++) {
            string += number[i];

            for (int j=0; j<str.length; j++) {
                if (string.equals(str[j])) {
                    ls.add(Long.toString(num[j]));
                    string = "";
                }
            }
        }

        for (int i = 0; i < ls.size(); i++) {
            string += ls.get(i);
        }

        return Long.parseLong(string);
    }
}
