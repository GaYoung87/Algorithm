import java.util.*;

public class Solution_20230218_같은숫자는싫어 {

    public int[] solution(int []arr) {
        ArrayList<Integer> array = new ArrayList<>();

        int front_val = -1;  // 0~9까지 이니까
        for (int i=0; i< arr.length; i++) {
            if (arr[i] != front_val) {
                array.add(arr[i]);
                front_val = arr[i];
            }
        }

        int[] answer = new int[array.size()];
        for (int i=0; i< answer.length; i++) {
            answer[i] = array.get(i);
        }
        return answer;
    }


}
