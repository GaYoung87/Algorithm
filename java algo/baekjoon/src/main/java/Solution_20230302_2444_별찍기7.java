import java.util.Scanner;

public class Solution_20230302_2444_별찍기7 {

    /**
     * 9 = 2*N-1이다 -> 이걸 기준으로 위에, 아래 따로따로 출력하기
     */
//    *     1(4)
//   ***    3(3)
//  *****   5(2)
// *******  7(1)
//********* 9
// *******  7(1)
//  *****   5(2)
//   ***    3(3)
//    *     1(4)

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i = 1; i <= N ; i++) {
            for(int j = 0; j < N-i; j++)
                System.out.print(" ");
            for(int j = 0; j < i*2-1; j++)
                System.out.print("*");
            System.out.println();
        }

        for(int i = N-1; i >= 0 ; i--) {
            for(int j = 0; j < N-i; j++)
                System.out.print(" ");
            for(int j = 0; j < i*2-1; j++)
                System.out.print("*");
            System.out.println();
        }
    }
}

