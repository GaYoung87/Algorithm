public class Solution_20230203_안전지대 {

    public int solution(int[][] board) {

        // 여기서 board는 n*n
        // System.out.println("board.length = " + board.length);
        // System.out.println("board[0].length = " + board[0].length);
        for (int x=0; x<board.length; x++) {
            for (int y=0; y<board.length; y++) {
                if (board[x][y] == 1){
                    check(x, y, board);
                }
            }
        }

        int answer = 0;
        for (int x=0; x<board.length; x++) {
            for (int y=0; y<board.length; y++) {
                if (board[x][y] == 0){
                    answer++;
                }
            }
        }

        return answer;
    }

    static void check(int x, int y, int[][] boardEx) {
        int nx;
        int ny;
        int[] nearX = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] nearY = {-1, 0, 1, -1, 1, -1, 0, 1};

        for (int i=0; i<8; i++) {
            nx = x + nearX[i];
            ny = y + nearY[i];
            if (nx >= 0 && nx < boardEx.length && ny >= 0 && ny < boardEx.length && boardEx[nx][ny]==0) {
                boardEx[nx][ny] = 2;
            }
        }
    }
}
