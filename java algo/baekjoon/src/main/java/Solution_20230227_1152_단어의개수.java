import java.util.Scanner;

public class Solution_20230227_1152_단어의개수 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        String words = in.nextLine();
        words = words.trim();  // trim(): 앞 뒤 공백 없앰
        String[] words_array = words.split(" ");
        if(words_array.length == 1 && words_array[0].equals("")) {
            System.out.println(0);
        }else {
            System.out.println(words_array.length);
        }
    }
}