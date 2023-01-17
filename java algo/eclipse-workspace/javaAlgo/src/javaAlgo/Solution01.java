package src.javaAlgo;

public class Solution01 {  // 옹알이(1)
	   
    String[] speakList = {"aya", "ye", "woo", "ma"};
    
    public int solution(String[] babbling) {
        
        int answer = 0;
        
        for (String bab : babbling) {
            for (String speak : speakList) {
                bab = bab.replace(speak, "?");
                //System.out.println(bab);
            }
            
            int flag = 0;
            for (int i=0; i<bab.length(); i++) {
                if (!bab.substring(i,i+1).equals("?")) {
                    flag = 1;
                }  // substring , indexOf , charAt 을 이용한 문자열 추출
            }
            //System.out.println(flag);
            if (flag == 0) {
                answer++;
            }
            
        }
        return answer;
    }

}
