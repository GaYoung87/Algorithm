import java.util.Scanner;

public class Solution_20230308_7568_덩치 {

    public static void main(String[] args) {
        // 몸무게, 키 모두 나보다 커야 덩치가 큰 것 -> RANK=1부터 시작
        // array = [[55,185],[55,183],[65,186],[60,175],[45,155]] -> [몸무게,키]
        //   val = [   1,        1,       0,       1,       4   ] -> 나보다 덩치큰사람
        // f_rank= [   2,        2,       1,       2,       5   ] -> 최종 rank
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] array = new int[n][2];
        for (int i=0; i<n; i++) {
            array[i][0] = in.nextInt();
            array[i][1] = in.nextInt();
        }

        // 나보다 덩치큰사람 찾기
        for (int i=0; i<n; i++) {
            int w = array[i][0];
            int h = array[i][1];
            int rank = 1;
            for (int j=0; j<n; j++) {
                if (i == j) {
                    continue;
                }
                if (w < array[j][0] && h < array[j][1]) {
                    rank++;
                }
            }
            System.out.println(rank);
        }
    }
}
