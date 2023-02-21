public class Solution_20230205_겸치는선분의길이_fail {

    public int solution(int[][] lines) {
        int answer = 0;

        int[] array = new int[200];

        for (int[] line : lines) {
            int my_min = Math.min(line[0], line[1]);
            int my_max = Math.max(line[0], line[1]);

            for (int i = my_min; i < my_max + 1; i++) {
                array[i+100]++;
            }
        }

        for (int i=1; i<array.length; i++ ) {
            if (array[i] > 1) {
                answer++;
            }
        }

        return answer;
    }
}
