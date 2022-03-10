def solution(id_list, report, k):
    report = set(report)
    report_result = {i: [] for i in id_list}
    warning_cnt = {i: 0 for i in id_list}

    for re in report:
        a, b = re.split(' ')
        report_result[a].append(b)
        warning_cnt[b] += 1

    check_people = []
    for name, cnt in warning_cnt.items():
        if cnt >= k:
            check_people.append(name)

    result = [0] * len(id_list)
    for id in id_list:
        for check in check_people:
            if check in report_result[id]:
                result[id_list.index(id)] += 1

    return result