public class Solution_20230202_캐릭터의좌표_2 {

     public int[] solution(String[] keyinput, int[] board) {
         int[] answer = {0, 0};

         //System.out.println();

         for (String key : keyinput) {
             if (key.equals("left")) {
                 answer[0]--;
                 if (answer[0] < -board[0]/2) {
                     answer[0]++;
                 }
             }
             if (key.equals("right")) {
                 answer[0]++;
                 if (answer[0] > board[0]/2) {
                     answer[0]--;
                 }
             }
             if (key.equals("down")) {
                 answer[1]--;
                 if (answer[1] < -board[1]/2) {
                     answer[1]++;
                 }
             }
             if (key.equals("up")) {
                 answer[1]++;
                 if (answer[1] > board[1]/2) {
                     answer[1]--;
                 }
             }
         }
         return answer;
     }
}
