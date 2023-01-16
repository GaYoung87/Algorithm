fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
           "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]  # [14600, 34400, 5000]
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]  # [0, 591]
# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]  # [14841]
import math


def changeToMinute(first, second):
    h1, m1 = map(int, first.split(':'))
    h2, m2 = map(int, second.split(':'))
    total1, total2 = h1 * 60 + m1, h2 * 60 + m2

    return total2 - total1;


def solution(fees, records):
    dt, df, ut, uf = fees
    check = {}
    check_time = {}
    for record in records:
        when, car, inout = record.split()
        if inout == "IN":
            check[car] = when
        else:
            if car not in check_time:
                check_time[car] = changeToMinute(check[car], when)
            else:
                check_time[car] += changeToMinute(check[car], when)
            check[car] = "0"
    print(check)
    print(check_time)
    for key, value in check.items():
        print(key, value)
        if value != "0":
            if key in check_time:
                check_time[key] += changeToMinute(value, "23:59")
            else:
                check_time[key] = changeToMinute(value, "23:59")  # 테스트3번에서 check_time에 아예 아무것도 안들어가있을 수도 있음

    check_time = sorted(check_time.items())

    answer = []
    for car, total_time in check_time:
        if total_time <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((total_time - dt) / ut) * uf)

    return answer