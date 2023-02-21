public class Solution_20230122_가장큰수찾기 {

    public int[] solution(int[] array) {
        int[] answer = new int[2];  // int[]에 몇개가 들어갈것인지 지정해줘야함

        int max_num = 0;
        int idx = 0;
        for (int i=0; i< array.length; i++) {
            if (max_num < array[i]) {
                max_num = array[i];
                idx = i;
            }
        }

        answer[0] = max_num;
        answer[1] = idx;

        return answer;
    }
}
