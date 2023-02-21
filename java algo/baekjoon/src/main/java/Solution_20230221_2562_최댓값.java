import java.util.Scanner;

public class Solution_20230221_2562_최댓값 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int mymax = -999999999;
        int idx = 0;
        int[] array = new int[9];
        for (int i=1; i<10; i++) {
            int num = in.nextInt();

            if (num > mymax) {
                mymax = num;
                idx = i;
            }
        }

        System.out.println(mymax + " " + idx);
    }
}
