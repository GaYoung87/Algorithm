public class Solution_20230122_문자열계산하기 {

    public int solution(String my_string) {
        int answer = 0;

        String[] array = my_string.split(" ");
        answer += Integer.parseInt(array[0]);

        boolean flag = true;
        for (int i=1; i<array.length; i++) {
            if (array[i].equals("+")) {
                flag = true;
            } else if (array[i].equals("-")) {
                flag = false;
            } else {
                if(flag) {
                    answer += Integer.parseInt(array[i]);
                } else {
                    answer -= Integer.parseInt(array[i]);
                }
            }
        }
        return answer;
    }

}
