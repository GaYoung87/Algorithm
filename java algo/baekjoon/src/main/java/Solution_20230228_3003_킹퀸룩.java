import java.util.Scanner;

public class Solution_20230228_3003_킹퀸룩 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8
        int king = 1 - in.nextInt();
        int queen = 1 - in.nextInt();
        int look = 2 - in.nextInt();
        int bi = 2 - in.nextInt();
        int knite = 2 - in.nextInt();
        int pon = 8 - in.nextInt();

        System.out.println(king +" "+queen+" "+look+" "+bi+" "+knite+" "+pon);
    }
}
