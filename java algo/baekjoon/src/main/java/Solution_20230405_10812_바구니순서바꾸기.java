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
        for (int i=0; i<m; i++) {
            int start = in.nextInt() - 1;
            int end = in.nextInt() - 1;
            int mid = in.nextInt() - 1;

            // mid~end
            for (int x=mid; x<=end; x++) {
                new_array[x-mid] = array[x];
            }

            // start~mid
            for (int x=start; x<mid; x++) {
                new_array[x+mid] = array[x];
            }

            array = new_array;

            for (int a: array) {
                System.out.print( a + " ");
            }
        }


    }
}
