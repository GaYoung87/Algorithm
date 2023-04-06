import java.util.Scanner;

public class Solution_20230314_10812_바구니순서바꾸기 {

    public static void main(String[] args) {

        /**
         * 10 5   -> 1 2 3 4 5 6 7 8 9 10
         *              [8 9 3 4 5 6 7]
         * 3 9 8  -> 1 2 8 9 3 4 5 6 7 10
         *          [4 5 6 1 2 3]
         * 1 6 4  -> 4 5 6 1 2 3 7 8 9 10
         *              [8 9 3 4 5 6 7]
         * 3 9 8  -> 4 5 8 9 6 1 2 3 7 10
         * 2 10 5 -> 4 6 1 2 3 7 10 5 8 9
         * 1 3 3  -> 1 4 6 2 3 7 10 5 8 9
         * 2 6 2  -> 1 4 6 2 3 7 10 5 8 9
         */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int[] array = new int[n];
        int[] new_array = new int[n];
        for (int i=0; i<n; i++) {
            array[i] = i+1;
            new_array[i] = i+1;
        }

        /**
         * 맨 처음에 array, new_array를 동일하게 둔다.
         * new_array를 mid~end~start 기준으로 array로부터 값을 가지고와서 바꾼다.
         * mid~end, start~mid로 나눠서 바꿔준다.
         */
        for (int i=0; i<m; i++) {
            int start = in.nextInt()-1;
            int end = in.nextInt()-1;
            int mid = in.nextInt()-1;

            //          [4 5 6 1 2 3]
            // 1 6 4  -> 4 5 6 1 2 3 7 8 9 10
            //              [8 9 3 4 5 6 7]
            // 3 9 8  -> 1 2 8 9 3 4 5 6 7 10
            // mid ~ end
            int k = 0;
            for (int j = mid; j<end+1; j++) {
                new_array[j-mid+start] = array[mid+k];
                k++;
            }

            // start ~ end
            //          [4 5 6 1 2 3]
            // 1 6 4  -> 4 5 6 1 2 3 7 8 9 10
            //              [8 9 3 4 5 6 7]
            // 3 9 8  -> 1 2 8 9 3 4 5 6 7 10
//            int z = 0;
            for (int j = start; j<mid; j++) {
                new_array[j+mid] = array[j];
//                z++;
            }


            array = new_array;

            for (int a: array) {
                System.out.print( a + " ");
            }
        }
    }
}
