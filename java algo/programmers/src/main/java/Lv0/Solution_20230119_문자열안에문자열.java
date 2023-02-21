public class Solution_20230119_문자열안에문자열 {  // 문자열안에 문자열

    public int solution(String str1, String str2) {
        if (str1.contains(str2)) {
            return 1;
        } else {
            return 2;
        }
    }
}
