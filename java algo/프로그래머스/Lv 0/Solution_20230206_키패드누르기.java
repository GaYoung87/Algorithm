public class Solution_20230206_키패드누르기 {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int leftL = 10;
        int rightL = 11;
        for (int i=0; i<numbers.length; i++) {
            if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
                answer += 'L';
                leftL = numbers[i];
            } else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
                answer += 'R';
                rightL = numbers[i];
            } else {
                int leftD = distance(leftL, numbers[i]);
                int rightD = distance(rightL, numbers[i]);

                if (leftD > rightD) {
                    rightL = numbers[i];
                    answer += 'R';
                } else if (leftD < rightD) {
                    leftL = numbers[i];
                    answer += 'L';
                } else {
                    if (hand.equals("left")) {
                        leftL = numbers[i];
                        answer += 'L';
                    } else {
                        rightL = numbers[i];
                        answer += 'R';
                    }
                }

            }
        }
        return answer;
    }

    public int distance(int x, int y) {
        int[][] keyboard = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 0, 11}};
        int[] xloc = new int[2];
        int[] yloc = new int[2];

        for (int i=0; i<4; i++) {
            for (int j=0; j<3; j++) {
                if (x == keyboard[i][j]) {
                    xloc[0] = i;
                    xloc[1] = j;
                }
                if (y == keyboard[i][j]) {
                    yloc[0] = i;
                    yloc[1] = j;
                }
            }
        }

        int dis = Math.abs(xloc[0]-yloc[0]) + Math.abs(xloc[1]-yloc[1]);
        return dis;

    }
}
