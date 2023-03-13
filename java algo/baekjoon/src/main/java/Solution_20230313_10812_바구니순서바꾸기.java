import java.util.Scanner;

public class Solution_20230313_10812_바구니순서바꾸기 {

    public static void main(String[] args) {

        /**
         * 10 5
         * 1 2 3 4 5 6 7 8 9 10
         * 1 6 4 -> 4 5 6 1 2 3 7 8 9 10
         * 3 9 8 -> 4 5 8 9 6 1 2 3 7 10
         * 2 10 5 -> 4 6 1 2 3 7 10 5 8 9
         * 1 3 3 -> 1 4 6 2 3 7 10 5 8 9
         * 2 6 2 -> 1 4 6 2 3 7 10 5 8 9
         * 1 4 6 2 3 7 10 5 8 9
         */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int[] array = new int[n];
        for (int i=0; i<n; i++) {
            array[i] = i+1;
        }

        for (int i=0; i<m; i++) {

        }
    }
}
