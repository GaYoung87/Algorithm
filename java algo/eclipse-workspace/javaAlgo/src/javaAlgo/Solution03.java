class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer = new String[my_str.length()/n];

        int start = 0;
        for (int i=0; i<my_str.length()/n+1; i++) {
            int end = n*(i+1);
            // String word = my_str.substring(start, end);
            // System.out.println(word);
            start = end;

            System.out.println(i);
            //answer[i] = word;  // 배열에 값 추가하는 방법 

        }
        return answer;
    }
}