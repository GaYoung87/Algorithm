import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * [ 자바 코딩 ] NumberFormatException 원인과 해결방법
 *      - https://jamesdreaming.tistory.com/126
 */
// A+B-5
public class Solution_20230221_10952_A더하기B_5 {

    public static void main(String[] args)  throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String st = br.readLine();
            String[] ss = st.split(" ");
            int A = Integer.parseInt(ss[0]);
            int B = Integer.parseInt(ss[1]);

            if (A == 0 && B == 0) {
                break;
            }

            System.out.println(A+B);
        }
    }
}
