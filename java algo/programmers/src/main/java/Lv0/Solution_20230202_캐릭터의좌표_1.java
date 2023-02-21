public class Solution_20230202_캐릭터의좌표_1 {

    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0, 0};

        for (String key : keyinput) {
            switch(key) {
                case "left": answer[0]--;
                    break;
                case "right": answer[0]++;
                    break;
                case "up": answer[1]++;
                    break;
                case "down": answer[1]--;
                    break;
            }

            // left는 -, right는 + 니까 범위 넘으면 left이면 +, right이면 -
            if (Math.abs(answer[0]) > board[0]/2) {
                answer[0] += (answer[0] > 0) ? -1 : 1;
            }
            // down는 -, up는 + 니까 범위 넘으면 down이면 +, up이면 -
            if (Math.abs(answer[1]) > board[1]/2) {
                answer[1] += (answer[1] > 0) ? -1 : 1;
            }

        }

        return answer;
    }
}
