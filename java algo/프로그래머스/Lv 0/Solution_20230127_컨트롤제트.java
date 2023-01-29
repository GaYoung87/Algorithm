public class Solution_20230127_컨트롤제트 {

    public int solution(String s) {

        int answer = 0;
        String[] array = s.split(" ");
        for (int i=0; i<array.length; i++) {
            if (array[i].equals("Z")) {
                array[i-1] = "0";
                array[i] = "0";

            }
        }

        for (int i=0; i<array.length; i++) {
            answer += Integer.parseInt(array[i]);
        }
        return answer;
    }
}
