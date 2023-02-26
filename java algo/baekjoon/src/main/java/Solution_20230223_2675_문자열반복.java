import java.util.Scanner;

public class Solution_20230223_2675_문자열반복 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        //  nextLine()은 엔터값을 입력받을 때까지 기준으로 한 줄을 읽어버려서 " ABC"로 읽음
        // 반면에 next()는 공백을 기준으로 하나의 문자열만 읽어서 "ABC"로 읽음.
        for (int i=0; i<n; i++) {
            int num = in.nextInt();
            String words = in.next();

            String answer = "";
            for (int j=0; j<words.length(); j++) {
                for (int k=0; k<num; k++) {
                    answer += words.charAt(j);
                }
            }
            System.out.println(answer);
        }
    }
}
