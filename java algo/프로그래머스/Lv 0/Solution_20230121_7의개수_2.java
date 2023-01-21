public class Solution_20230121_7의개수_2 {

    public int solution(int[] array) {
        int answer = 0;

        for (int i=0; i<array.length; i++) {
            String word = Integer.toString(array[i]);
            String[] arr = word.split("");  // ["7"], ["7","7"], ["1","7"]
                                                  // List, ArrayList, String[]의 차이

            for (int j=0; j<arr.length; j++) {
                if (arr[j].equals("7")) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}
