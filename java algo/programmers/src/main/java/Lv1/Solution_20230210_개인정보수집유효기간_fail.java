import java.util.ArrayList;

/**
 * today = "2022.05.19"
 * terms = ["A 6", "B 12", "C 3"]
 * privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
 * ----------------------------------------------------------------------------------
 * 1. privacies을 돌리면서 ["2021.05.02", "A"]로 잘라서 makeDay함수에서 "2021.11.02"로 만들어줌
 * 2. 이때 ["2021", "05", "02"](x)로 쪼개서
 * 3. makeDay 함수에서 pri돌면서 terms에 따라 더하기(check함수)
 *    -> ["yyyy","mm","dd"] -> "2021.11.02"
 * 3. 끝에 비교할 때 "20220519", "20211102"로 만들어서 비교
 */

public class Solution_20230210_개인정보수집유효기간_fail {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        today = today.replaceAll("[.]","");

        for (int i=0; i< privacies.length; i++) {
            String[] pri = privacies[i].split(" ");  // ["2021.05.02", "A"]
            String[] x = pri[0].split("[.]");  // ["2021", "05", "02"] -> 왜 "."은 안되나?
            String y = pri[1];

            String temp = makeDay(x, y, terms);
//            System.out.println("today = " + today);
//            System.out.println("temp = " + temp);
//            System.out.println("today.compareTo(temp) = " + today.compareTo(temp));
            if (today.compareTo(temp) >= 0) {

                answer.add(i+1);
            }

        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    public String makeDay(String[] a, String b, String[] terms) {
        String result = "";

        for (int i=0; i < terms.length; i++) {
            String[] term = terms[i].split(" ");

            if (term[0].equals(b)) {

                int month = Integer.parseInt(term[1]);
                int a1_num = Integer.parseInt(a[1]) + month;
                System.out.println("a1_num = " + a1_num);

                int mok = 0;
                while (a1_num > 12) {
                    a1_num %= 12;
                    mok++;
                    System.out.println("whilemok = " + mok);
                }
                System.out.println("firstmok = " + mok);
                int na = a1_num;
                if (na == 0) {
                    na = 12;
                }
                System.out.println("a1_num = " + a1_num);
                System.out.println("mok = " + mok);
                System.out.println("na = " + na);
                a[0] = Integer.toString(Integer.parseInt(a[0]) + mok);
                a[1] = Integer.toString(na);

                System.out.println("yyyy = " + a[0]);

                if (a[1].length() == 1) {
                    a[1] = "0" + a[1];
                }
                System.out.println("mm = " + a[1]);
            }
        }

        for (String aa : a) {
            result += aa;
        }

        return result;
    }
}
