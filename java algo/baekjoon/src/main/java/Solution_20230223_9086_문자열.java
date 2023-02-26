import java.util.Scanner;

public class Solution_20230223_9086_문자열 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        /**
         next(): 문자 또는 문자열을 공백을기준으로 한단어 또는 한문자씩 입력받음
         nextLine(): 문자 또는 문장 한라인 전체를 입력받는다.
         Hello java-> next(): Hello, nextLine(): Hello java
         */
        for (int i=0; i<n ; i++) {
            String x = in.next();   // String으로 가지고옴
            /**if (x.length() <= 1) {
             System.out.println(x + "" + x);
             } else {*/
            String first = x.substring(0,1);
            String end = x.substring(x.length()-1, x.length());
            System.out.println(first + end);
            //}
        }
    }
}
