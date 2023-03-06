import java.util.Scanner;

public class Solution_20230305_2566_최댓값 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[][] arr = new int[9][9];
        int mymax = -1;
        int x = 0;
        int y = 0;
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                arr[i][j] = in.nextInt();
                if (mymax < arr[i][j]) {
                    mymax = arr[i][j];
                    x = i;
                    y = j;
                }
            }
        }

        System.out.println(mymax);
        System.out.print((x+1) + " " + (y+1));

    }
}
