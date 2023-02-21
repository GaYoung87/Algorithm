import java.util.ArrayList;
import java.util.Scanner;

public class Solution_20230221_10871_X보다작은수 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int X = in.nextInt();
        int[] array = new int[N];

        for (int i=0; i<N; i++) {
            array[i] = in.nextInt();
        }

        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=0; i<N; i++) {
            if (X > array[i]) {
                answer.add(array[i]);
            }
        }

        for (int i=0; i< answer.size(); i++) {
            System.out.println(answer.get(i));
        }
    }
}
