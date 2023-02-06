public class Solution_20230206_숫자문자열과영단어 {

    public int solution(String s) {
        String[] numbers = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for(int i = 0; i < numbers.length; i++){
            s = s.replace(numbers[i], Integer.toString(i));
        }

        return Integer.parseInt(s);
    }
}
