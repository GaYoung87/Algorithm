public class Solution_20230220_시저암호 {

    public String solution(String s, int n) {
        String answer = "";
        String[] ss = s.split("");

        for (int i=0; i<ss.length; i++) {
            String word = ss[i];
            System.out.println("word.charAt() = " + word.charAt());

            if (word.equals(" ")) {
                answer += word;
            }

        }
        return answer;
    }
}
