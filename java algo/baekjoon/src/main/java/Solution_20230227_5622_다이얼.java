import java.util.Scanner;

public class Solution_20230227_5622_다이얼 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        String word = in.next();
        int[] alpha = new int[26];
        alpha[0] = alpha[1] = alpha[2] = 3; //A, B, C는 각각 3초가 걸린다
        alpha[3] = alpha[4] = alpha[5] = 4; //D, E, F는 4초가 걸린다 
        alpha[6] = alpha[7] = alpha[8] = 5;
        alpha[9] = alpha[10] = alpha[11] = 6;
        alpha[12] = alpha[13] = alpha[14] = 7;
        alpha[15] = alpha[16] = alpha[17] = alpha[18] = 8;
        alpha[19] = alpha[20] = alpha[21] = 9;
        alpha[22] = alpha[23] = alpha[24] = alpha[25] = 10;

        int answer = 0;
        for (int i=0; i<word.length(); i++ ){
            char x = word.charAt(i);
            answer += alpha[x-65];
        }

        System.out.println(answer);
    }
}
