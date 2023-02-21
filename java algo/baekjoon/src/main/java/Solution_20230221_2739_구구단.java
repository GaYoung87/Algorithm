import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

// 구구단
public class Solution_20230221_2739_구구단 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int a = in.nextInt();

        in.close();

        for(int i = 1; i<10;i++) {
            System.out.println(a+" * "+i+" = "+(a*i));
        }
    }

    public static void main2(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        br.close();

        for(int i = 1; i<10;i++) {
            System.out.println(a+" * "+i+" = "+(a*i));
        }
    }
}
