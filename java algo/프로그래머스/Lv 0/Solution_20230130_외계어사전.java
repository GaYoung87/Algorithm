public class Solution_20230130_외계어사전 {

    /**
     * spell	              dic	                                  result
     * ["p", "o", "s"]	    ["sod", "eocd", "qixm", "adio", "soo"]	    2
     * ["z", "d", "x"]	    ["def", "dww", "dzx", "loveaw"]             1
     * ["s", "o", "m", "d"]	["moos", "dzx", "smm", "sunmmo", "som"]	    2
     */
    public int solution(String[] spell, String[] dic) {

        int answer = 0;

        for (String d : dic) {

            boolean flag = true;
            for (String s : spell) {
                if (d.indexOf(s) == -1) {  // 포함x
                    flag = false;
                    answer = 2;
                    break;
                }
            }

            if (flag) {
                answer = 1;
                break;
            }
        }
        return answer;
    }
}
