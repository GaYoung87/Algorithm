import java.util.Scanner;

public class Solution_20230305_10798_세로읽기 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        char[][] arr = new char[5][15];
        for (int i=0; i<5; i++) {
            String word = in.next();
            for (int j=0; j<word.length(); j++) {
                arr[i][j] = word.charAt(j);  // 입력받은 문자열 넣기(최대15개니까 남는단어도 있음)
            }
        }

        StringBuilder answer = new StringBuilder();
        for (int x=0; x<15; x++) {
            for (int y=0; y<5; y++) {
                // 빈칸(공백이거나 null)이면 continue
                if (arr[y][x] == '\0') {
                    continue;
                } else {  // 빈칸이 아니면 answer에 추가
                    answer.append(arr[y][x]);
                }
            }
        }

        System.out.println(answer);
    }
}
