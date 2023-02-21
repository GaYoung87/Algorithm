import java.util.HashMap;
import java.util.HashSet;

public class Solution_20230209_신고결과받기 {

    /**
     *    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
     * => ["muzi": ["appeach"], "frodo": ["muzi","appeach"], "apeach": [], "neo": ["muzi", "frodo"]]
     * => []안의 갯수가 k개 이상이면 []를 돌리면서
     * => [m, f, a, n]기준으로 [2, 1, 1, 0]으로 보여줌
     */

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];

        // Set, HashSet의 차이
        HashMap<String, HashSet<String>> reportArray = new HashMap<>();
        // mail_name="m"이면 answer[0]++ 해주려고 idxArray 만듦
        HashMap<String, Integer> idxArray = new HashMap<>();

        // reportArray=["muzi": [], "frodo": [], "apeach": [], "neo": []] 틀 만들기
        for (int i=0; i<id_list.length; i++) {
            reportArray.put(id_list[i], new HashSet<>());
            idxArray.put(id_list[i], i);
        }

        // reportArray=["muzi": ["appeach"], "frodo": ["muzi","appeach"], "apeach": [], "neo": ["muzi", "frodo"]]로 이름 넣기
        for (String r : report) {
            String[] people = r.split(" ");
            reportArray.get(people[1]).add(people[0]);
        }

        // reportArray의 value값의 갯수세기
        for (int i=0; i< id_list.length; i++) {
            HashSet<String> mail = reportArray.get(id_list[i]);
            System.out.println("mail.size() = " + mail.size());
            if (mail.size() >= k) {
                for (String mail_name : mail) {
                    // mail_name="m"이면 answer[0]++ 해줘야함 -> idxArray 만들어줌
                    answer[idxArray.get(mail_name)]++;
                }
            }
        }

        return answer;
    }

}
