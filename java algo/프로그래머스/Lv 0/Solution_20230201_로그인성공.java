public class Solution_20230201_로그인성공 {

    public String solution(String[] id_pw, String[][] db) {
        String id = id_pw[0];
        String pw = id_pw[1];

        String answer = "";
        for (int i=0; i<db.length; i++) {
            if (id.equals(db[i][0])) {
                if (pw.equals(db[i][1])) {
                    answer = "login";
                    break;
                } else {
                    answer = "wrong pw";
                }

                // 에러! 이런경우에 만약에 db길이가 1인데, id가 일치하지않으면 위에 if문에서 answer=""가 됨
                // } else {
                //     answer = "fail";
                // }

                // 방법1. login, wrong pw아니면 fail
                //    } else {
                //        if (!answer.equals("login") && !answer.equals("wrong pw")){
                //            answer = "fail";
                //         }
                //    }
            }
        }

        // 방법2. 최종적으로 login, wrong pw가 아니라 ""이면 fail
        if (answer == "") {
            answer = "fail";
        }
        return answer;
    }
}
