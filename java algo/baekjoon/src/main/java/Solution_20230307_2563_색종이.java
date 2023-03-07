import java.util.Scanner;

public class Solution_20230307_2563_색종이 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[][] board = new int[100][100];

        int T = in.nextInt();
        for (int t=0; t<T; t++) {
            int a = in.nextInt() - 1;
            int b = in.nextInt() - 1;

            for (int x = a; x < a + 10; x++) {
                for (int y = b; y < b + 10; y++) {
                    if (board[x][y] == 0) {
                        board[x][y] = 1;
                    }
                }
            }
        }

        int count = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (board[i][j] == 1) {
                    count++;
                }
            }
        }

        System.out.println(count);

    }
}
