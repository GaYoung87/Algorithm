public class Solution_20230210_비밀지도 {

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i=0; i < n; i++) {
            String[] make_arr1 = makeNumber(arr1[i], n);
            String[] make_arr2 = makeNumber(arr2[i], n);

            String temp = "";
            for (int j=0; j < n; j++) {
                // "1".equals(make_arr1[j]) vs make_arr1[j].equals("1")의 차이
                if ("1".equals(make_arr1[j]) || "1".equals(make_arr2[j])) {
                    temp += "#";
                } else {
                    temp += " ";
                }
            }

            answer[i] = temp;
        }

        return answer;
    }

    // 이진수로 만들면서 이걸 문자로 가지고오기
    // x=9 -> result = "01001" -> ["0", "1", "0", "0", "1"]로 바꾸기(나주에 make_arr1[j]로 편하게 하려고)
    public String[] makeNumber(int x, int total_len) {
        String result = "";

        while (x > 0) {
            result = x % 2 + result;
            x /= 2;
        }

        for (int i=result.length(); i<total_len; i++) {
            result = "0" + result;
        }
        return result.split("");
    }
}
