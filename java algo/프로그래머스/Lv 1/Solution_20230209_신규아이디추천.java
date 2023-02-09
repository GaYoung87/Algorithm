public class Solution_20230209_신규아이디추천 {

    public String solution(String new_id) {
        /*
        1. 대문자-> 소문자 치환
        2. 정규표현식
        3. substring의 index
        */
        // 1단계 소문자로 치환
        String answer = new_id.toLowerCase();

        // 2단계 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한(^) 모든 문자 제거
        answer = answer.replaceAll("[^a-z0-9-_.]", "");

        // 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
        answer = answer.replaceAll("[.]{2,}", "."); // answer.replaceAll("[.]{2}", ".");와의 차이는?

        // 4단계 마침표(.)가 처음이나 끝에 위치한다면 제거
        if (answer.length() > 0 && answer.charAt(0)=='.') {
            answer = answer.substring(1);
        }
        if (answer.length() > 0 && answer.charAt(answer.length()-1)=='.') {
            answer = answer.substring(0, answer.length()-1);
        }

        // 5단계 빈 문자열이라면, new_id에 "a"를 대입합니다.
        if (answer.length() == 0) {
            answer = "a";
        }

        // 6단계 길이가 16자 이상이면, 15개 문자까지만 표시.
        //       만약 제거 후 마침표(.)가 끝이라면 마침표(.) 문자를 제거
        if (answer.length() >= 16) {
            answer = answer.substring(0, 15);
            if (answer.charAt(answer.length()-1)=='.') {
                answer = answer.substring(0, answer.length()-1);
            }
        }

        // 7단계 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
        if (answer.length() <= 2) {
            int idx = answer.length();
            while (idx < 3) {
                answer += answer.charAt(answer.length()-1);
                idx++;
            }
        }


        System.out.println(answer);
        return answer;
    }
}
