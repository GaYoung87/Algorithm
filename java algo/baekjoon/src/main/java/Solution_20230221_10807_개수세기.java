import java.util.Scanner;

public class Solution_20230221_10807_개수세기 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] array = new int[n];

        for(int i = 0; i < n; i++) {
            array[i] = in.nextInt();
        }

        int num = in.nextInt();

        int answer = 0;
        for (int i=0; i<n; i++) {
            if (num == array[i]) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}
