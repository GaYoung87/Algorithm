import java.util.Scanner;

public class Solution_20230221_10818_최소최대 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int mymin = 999999999;
        int mymax = -999999999;

        for (int i=0; i<n; i++) {
            int num = in.nextInt();

            if (num < mymin) {
                mymin = num;
            }

            if (num > mymax) {
                mymax = num;
            }
        }

        System.out.println(mymin + " " + mymax);
    }
}
