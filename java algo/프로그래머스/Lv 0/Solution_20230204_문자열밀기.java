public class Solution_20230204_문자열밀기 {

    public int solution(String A, String B) {
        int answer = 0;

        for (int i=0; i<A.length(); i++) {
            if (A.equals(B)) {
                return answer;
            }

            String subA = A.substring(A.length()-1);
            // System.out.println("subA = " + subA);
            A = subA + A.substring(0, A.length()-1);
            // System.out.println("A = " + A);
            answer++;

        }
        return -1;
    }

}
