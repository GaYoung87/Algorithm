public class Solution_20230202_다항식더하기 {

    public String solution(String polynomial) {
        String answer = "";
        String[] p_list = polynomial.split(" \\+ ");
        /**
         * polynomial.split(" ")        polynomial.split("\\+")
         3x                            3x
         +                         (한칸띄고)7
         7                         (한칸띄고)x
         +
         x
         */

        int x_param = 0;
        int param = 0;
        for (String p : p_list) {
            //System.out.println(p);
            if (p.contains("x")) {
                //System.out.println(p.substring(0,p.length()-1));
                if (p.substring(0,p.length()-1).equals("")) {
                    x_param += 1;
                } else {
                    x_param += Integer.parseInt(p.substring(0,p.length()-1));
                }
            } else {
                if (!p.contains("+")) {
                    param += Integer.parseInt(p.substring(0,p.length()));
                }
            }
        }
//         System.out.println(x_param);
//         System.out.println(param);

        /*
        경우1. 2x
        경우2. 0
        경우3. 2x + 7

        주의!! 1x가 아닌 x이다!!
        */
        if (x_param != 0 && x_param != 1 && param != 0) {
            answer = Integer.toString(x_param) + "x + " + Integer.toString(param);
        }
        if (x_param != 0 && x_param != 1 && param == 0) {
            answer = Integer.toString(x_param) + "x";
        }
        if (x_param == 1 && param == 0) {
            answer = "x";
        }
        if (x_param == 1 && param > 0) {
            answer = "x + " + Integer.toString(param);
        }
        if (x_param == 0) {
            answer = Integer.toString(param);
        }

        System.out.println(answer);

        return answer;
    }
}
