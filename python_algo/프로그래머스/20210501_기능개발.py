import math 

def solution(progresses, speeds):
    time = []
    len_progresses = len(progresses)
    for i in range(len_progresses):
        count = math.ceil((100 - progresses[i]) / speeds[i])
        time.append(count)
    
    answer = []
    days = 0
    for idx in range(len(time)):
        if time[days] < time[idx]:
            answer.append(idx - days)
            days = idx
    answer.append(len(time) - days)  # 마지막 days를 기준으로 answer에 넣기
    
    return answer