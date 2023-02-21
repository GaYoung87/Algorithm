public class Solution_20230123_숨어있는숫자의덧셈2_1 {

    /*
    my_string = "aAb1B2cC34oOp"	// 37
    my_string = "1a2b3c4d123Z"	// 133
    */

    /*
    * 방법1. 문자 다 제거 -> 남아있는 숫자 더하기
    * 방법2. 하나하나 돌면서 문자면 pass, 숫자면 다음값도 숫자인지 확인해서 answer에 더하고,
    * */
    public int solution(String my_string) {

        String[] split_string = my_string.split("[a-zA-Z]");  // 매개변수로 들어온 문자열을 대소문자 알파벳을 기준으로 스플릿

        int answer = 0;
        for (int i=0; i<split_string.length; i++) {
            /* _
               _
               _
               1
               2
               _
               34
            */
            if (split_string[i].equals("")) {
                continue;
            } else {
                answer += Integer.parseInt(split_string[i]);
            }
        }
        return answer;
    }

}
