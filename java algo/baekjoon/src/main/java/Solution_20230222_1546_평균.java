import java.util.Scanner;

public class Solution_20230222_1546_평균 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        float mymax = -999999999;
        float[] array = new float[n];
        for (int i = 0; i < n; i++) {
            array[i] = in.nextInt();
            if (array[i] > mymax) {
                mymax = array[i];
            }
        }

        float avg = 0;
        for (int i = 0; i < n; i++) {
            avg += (array[i]/mymax*100);
        }

        System.out.println(avg/n);
    }
}
