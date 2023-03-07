import java.util.Scanner;

public class Solution_20230307_2798_블랙잭 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int val = in.nextInt();
        int[] array = new int[n];

        for (int i=0; i<n; i++) {
            array[i] = in.nextInt();
        }

        int answer = 0;
        for (int x=0; x<n-2; x++) {
            for (int y=x+1; y<n-1; y++) {
                for (int z=y+1; z<n; z++) {
                    int temp = array[x] + array[y] + array[z];  // 세개 더한 값
                    // 더한값이 지정값보다 작거나 같아야하고, 기존값보다는 커야한다.
                    if (temp <= val && answer < temp) {
                        answer = temp;
                    }
                }
            }
        }

        System.out.println(answer);

    }
}
