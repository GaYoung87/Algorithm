import java.util.Scanner;

public class Solution_20230221_10810_공넣기 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int[] array = new int[n];
        for (int mm =0; mm<m; mm++) {
            int i = in.nextInt();
            int j = in.nextInt();
            int k = in.nextInt();

            for (int a=i-1; a<j; a++) {
                array[a] = k;
            }
        }

        for (int e=0; e<n; e++) {
            System.out.println(array[e]);
        }

    }
}
