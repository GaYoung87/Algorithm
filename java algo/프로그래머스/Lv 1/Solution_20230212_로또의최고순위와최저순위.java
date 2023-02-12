import java.util.Arrays;
import java.util.Collections;

public class Solution_20230212_로또의최고순위와최저순위 {

    /**
     *
     * @param lottos
     * @param win_nums
     * @return
     *
     * lottos 오름차순 정렬, win_nums 오름차순 정렬 후
     * lottos가  win_nums랑 같으면 temp++, 작으면면 break;하고 다음 값 가기
     * 이때 lottos에서 0갯수 세기
     * min = temp, max = temp + 0개수
     *
     */
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        Arrays.sort(lottos);    // [0, 0, 1, 25, 31, 44]
        Arrays.sort(win_nums);  // [1, 6, 10, 19, 31, 45]

        int cnt_zero = 0;
        int temp = 0;
        for (int i=0; i < lottos.length; i++) {
            if (lottos[i] == 0) {
                cnt_zero++;
            } else {
                for (int j=0; j < win_nums.length; j++) {
                    if (lottos[i] == win_nums[j]) {
                        temp++;
                    } else if (lottos[i] < win_nums[j]) {
                        break;
                    }
                }
            }
        }

        int mymin = temp;
        int mymax = temp + cnt_zero;

        System.out.println("mymin = " + mymin);
        System.out.println("mymax = " + mymax);

        answer[0] = check(mymax);
        answer[1] = check(mymin);

        return answer;
    }

    public int check(int x) {

        int result = 0;
        switch (x) {
            case 6:
                result = 1;
                break;
            case 5:
                result = 2;
                break;
            case 4:
                result = 3;
                break;
            case 3:
                result = 4;
                break;
            case 2:
                result = 5;
                break;
            case 1:
                result = 6;
                break;
            case 0:
                result = 6;
                break;
        }

        return result;
    }

}
