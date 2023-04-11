import java.util.Scanner;

public class Solution_20230411_2869_달팽이는올라가고싶다 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int v = in.nextInt();

        int answer = (v-b)/(a-b);
        if ((v-b)%(a-b) != 0) {
            answer++;
        }

        System.out.println(answer);
    }
}
