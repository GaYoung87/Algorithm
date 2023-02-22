import java.util.HashSet;
import java.util.Scanner;

public class Solution_20230222_3052_나머지 {

    public static void main(String[] args) {

        HashSet<Integer> array = new HashSet<>();
        Scanner in = new Scanner(System.in);
        for (int i=0; i<10; i++) {
            int na = in.nextInt() % 42;
            array.add(na);
        }

        System.out.println(array.size());
    }
}
