import java.util.Scanner;

public class Solution_20230222_5597_과제안내신분 {

    public static void main(String[] args) {
        int[] array = new int[30];
        Scanner in = new Scanner(System.in);
        for (int i=0; i<28; i++) {
            int x = in.nextInt();
            array[x-1]++;
        }

        for (int i=0; i<30; i++) {
            if(array[i] == 0) {
                System.out.println(i+1);
            }
        }
    }
}
