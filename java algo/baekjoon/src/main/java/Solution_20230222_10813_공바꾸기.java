import java.util.Scanner;

public class Solution_20230222_10813_공바꾸기 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int[] array = new int[n];
        for (int nn = 0; nn<n; nn++) {
            array[nn] = nn+1;
        }

        for (int mm =0; mm<m; mm++) {
            int i = in.nextInt();
            int j = in.nextInt();

            int temp1 = array[i-1];
            int temp2 = array[j-1];

            array[i-1] = temp2;
            array[j-1] = temp1;
        }

        for (int e=0; e<n; e++) {
            System.out.println(array[e]);
        }

    }
}
