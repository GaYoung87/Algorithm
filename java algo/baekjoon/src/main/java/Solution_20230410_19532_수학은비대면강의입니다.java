import java.util.Scanner;

public class Solution_20230410_19532_수학은비대면강의입니다 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();
        int c=in.nextInt();
        int d=in.nextInt();
        int e=in.nextInt();
        int f=in.nextInt();

        int X=0;
        int Y=0;
        for(int i=-999; i<1000; i++){
            for(int j=-999; j<1000; j++){
                if((a*i+b*j==c)&&(d*i+e*j==f)){
                    X=i;
                    Y=j;
                    break;
                }
            }
        }
        System.out.println(X +" "+Y);
    }
}
