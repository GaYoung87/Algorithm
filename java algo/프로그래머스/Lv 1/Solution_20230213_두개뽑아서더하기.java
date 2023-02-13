import java.util.*;

public class Solution_20230213_두개뽑아서더하기 {

    /**
     * [ 풀이과정 ]
     * numbers를 두번돌리면서 두개를 더해준 다음에 list인 array에 값이 없으면 넣어준다
     * 오름차순으로 정렬
     * ArrayList를 int로 변경하기
     */
    public int[] solution(int[] numbers) {
        int[] answer = {};
        List<Integer> array = new ArrayList<>();

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int temp = numbers[i] + numbers[j];

                if (!array.contains(temp)) {
                    array.add(temp);
                }
            }
        }

        answer = array.stream().mapToInt(i -> i).toArray();
        Arrays.sort(answer);

        return answer;
    }
    
}
