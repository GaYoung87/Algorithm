def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    answer = [0, 0]
    dis_ls = []

    def dfs(tmp, d): # 모든 경우의 할인율 조합을 구함
        if d == len(tmp):
            dis_ls.append(tmp[:])
            return
        else:
            for i in discount:
                tmp[d] += i
                dfs(tmp, d+1)
                tmp[d] -= i
    dfs([0]*len(emoticons), 0)

    for dis in dis_ls:
        cnt = 0
        money = 0
        for u in users:
            p_money = 0  # 개인 구매비용
            for j in range(len(dis)):
                if u[0] <= dis[j]:
                    p_money += emoticons[j]  * (100 - dis[j]) / 100
                if p_money >= u[1]:  # 도중에라도 넘으면 stop
                    break

            # print(p_money)

            if p_money >= u[1]:  # 제한금액 초과시 이모티콘 플러스 가입
                p_money = 0
                cnt += 1
            money += p_money

            # 갱신
        if cnt >= answer[0]:
            if cnt == answer[0]:
                answer[1] = max(answer[1], money)
            else:
                answer[1] = money
            answer[0] = cnt
    return answer

