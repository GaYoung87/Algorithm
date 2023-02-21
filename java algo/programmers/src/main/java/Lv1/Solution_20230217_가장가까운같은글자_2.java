/**
 * 맨 처음 글자는 무조건 -1이다.
 * 그다음부터는 lastIndexOf를 사용해 i-1 인덱스를 기준으로 있는지 없는지 확인
 * x값이 -1이면 -1을 넣고, 아니라면 기존 위치의 인덱스에서 존재하는 인덱스의 값을 빼서 넣으면 됨
 */

// lastIndexOf
public class Solution_20230217_가장가까운같은글자_2 {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];

        answer[0] = -1;
        for (int i=1; i<s.length(); i++) {
            int x = s.lastIndexOf(s.substring(i,i+1), i-1);
            System.out.println("x = " + x);

            if (x == -1)  { // 해당 값이 없으면 -1, 있으면 마지막에 위치한 문자의 index 알려줌
                answer[i] = x;
            } else {
                answer[i] = i-x;
            }
        }

        return answer;

    }
}
