public class Solution_20230220_시저암호 {

    /**
     * @param s
     * @param n
     * @return
     *
     * char 와 int간의 형변환 https://godsu94.tistory.com/167
     * [ 진행방법 ]
     * CHAR의 경우에는 숫자와 더하면 숫자로 나오고, 이를 (char)로 변환해주면 char로 바뀜
     * z의 경우 +1이 되면 a로 가야하므로 26(문자 a~z갯수)을 빼준다
     * Z도 동일
     */
    public String solution(String s, int n) {
        String answer = "";

        for (int i=0; i<s.length(); i++) {
            char word = s.charAt(i);

            if (word == ' ') {
                answer += word;
            }

            // 소문자
            if (word >= 'a' && word <= 'z') {
                if (word + n > 'z') {
                    answer += (char)(word-26+n);
                    System.out.println("word+n = " + (char)(word-26+n));
                } else {
                    answer += (char)(word+n);
                    System.out.println("word+n = " + (char)(word+n));
                }
            }

            // 대문자
            if (word >= 'A' && word <= 'Z') {
                if (word + n > 'Z') {
                    answer += (char)(word-26+n);
                    System.out.println("word+n = " + (char)(word-26+n));
                } else {
                    answer += (char)(word+n);
                    System.out.println("word+n = " + (char)(word+n));
                }
            }

        }
        return answer;
    }
}
