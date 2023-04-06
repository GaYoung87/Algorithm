import java.util.Scanner;

public class Solution_20230405_10812_바구니순서바꾸기 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int[] array = new int[n];
        int[] new_array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = i + 1;
            new_array[i] = i + 1;
        }

        /**
         * 10 5   -> 1 2 3 4 5 6 7 8 9 10
         *          [4 5 6 1 2 3]
         * 1 6 4  -> 4 5 6 1 2 3 7 8 9 10
         *              [8 9 3 4 5 6 7]
         * 3 9 8  -> 4 5 8 9 6 1 2 3 7 10
         * 2 10 5 -> 4 6 1 2 3 7 10 5 8 9
         * 1 3 3  -> 1 4 6 2 3 7 10 5 8 9
         * 2 6 2  -> 1 4 6 2 3 7 10 5 8 9
         */

        for (int i = 0; i < m; i++) {
            int start = in.nextInt() - 1;
            int end = in.nextInt() - 1;
            int mid = in.nextInt() - 1;

            // start~end까지 돌면서
            // end가 넘지 않으면(mid+x<=end) 되면, array의 mid~end를 new_array의 start~mid까지 넣고
            // 넘는다면, array의 start~mid를 new_array의 mid~end로 넣어주기
            int idx = start;
            for (int x = 0; x < end - start + 1; x++) {
                if (mid + x <= end) {
                    new_array[start + x] = array[mid + x];
                } else {
                    new_array[start + x] = array[idx];
                    idx++;
                }
            }

            for (int a = 0; a < n; a++) {
                array[a] = new_array[a];
            }
        }

        for (int a : array) {
            System.out.print(a + " ");
        }
    }
}
