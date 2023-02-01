import java.util.ArrayList;
import java.util.List;

public class Solution_20230131_소인수분해 {

    public int[] solution(int n) {
        int[] answer = {};
        List<Integer> array = new ArrayList<>();

        int idx = 2;
        while (n > 1) {
            if (n % idx == 0) {
                if (!array.contains(idx)) {
                    array.add(idx);
                }

                n /= idx;
            } else {
                idx++;
            }

        }

//        for (int i=0; i< array.size(); i++) {
//            answer.
//        }
        answer = array.stream().distinct().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}
