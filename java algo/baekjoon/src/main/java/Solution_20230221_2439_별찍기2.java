import java.util.Scanner;

// 별찍기2
public class Solution_20230221_2439_별찍기2 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();

        for (int i=1; i<n+1; i++) {
            for (int j=1; j < n-i+1; j++) {
                System.out.println(" ");
            }

            for (int j=0; j < i+1; j++) {
                System.out.println("*");
            }
            System.out.println("\n");
        }
    }
}