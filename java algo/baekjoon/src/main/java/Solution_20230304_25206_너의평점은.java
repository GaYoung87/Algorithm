import java.util.Scanner;

public class Solution_20230304_25206_너의평점은 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        double totalScore = 0;
        double totalGrade = 0;

        for (int t=0; t<5; t++) {
            String[] array = in.nextLine().split(" ");

            String score = array[1];
            String grade = array[2];

            if (!grade.equals("P")) {
                totalScore += check(Double.parseDouble(score), grade);
                totalGrade += Double.parseDouble(score);
            }
        }

        if (totalScore != 0) {
            totalScore /= totalGrade;
        }

        System.out.println(totalScore);
    }

    private static double check(double score, String word) {
        double sum = 0;
        switch (word) {
            case "A+":
                sum = score * 4.5;
                break;
            case "A0":
                sum = score * 4.0;
                break;
            case "B+":
                sum = score * 3.5;
                break;
            case "B0":
                sum = score * 3.0;
                break;
            case "C+":
                sum = score * 2.5;
                break;
            case "C0":
                sum = score * 2.0;
                break;
            case "D+":
                sum = score * 1.5;
                break;
            case "D0":
                sum = score * 1.0;
                break;
            case "F":
                sum = score * 0.0;
                break;
        }
        return sum;
    }

}
