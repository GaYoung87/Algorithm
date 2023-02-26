import java.util.Scanner;

// https://deftkang.tistory.com/55
// [Java] Scanner 클래스 사용법과 next(), nextLine()메소드의 차이
public class Solution_20230223_11654_아스키코드 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int x = (int)in.nextLine().charAt(0);   // String으로 가지고옴

        System.out.println(x);
    }
}
