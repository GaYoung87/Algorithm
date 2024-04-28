def solution(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#',
                                                                                                                 'b')

    music_ls = []
    for i in musicinfos:
        st, end, name, music = i.split(',')
        h1, m1 = st.split(':')
        h2, m2 = end.split(':')
        time = change_time(h2, m2) - change_time(h1, m1)
        music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#',
                                                                                                          'a').replace(
            'B#', 'b')
        print(music)
        if time < len(music):
            music = music[:time]
        else:
            mok, na = divmod(time, len(music))
            music = mok * music + music[:na]
        music_ls.append([time, name, music])
    print(music_ls)

    # 조건 일치하는 음악 찾기
    music_length = 0
    check = []
    for ls in music_ls:
        if m in ls[2]:
            if ls[0] > music_length:
                music_length = ls[0]
                check.append(ls)
    print(check)
    # 제목 확인
    if len(check) == 0:
        return "(None)"
    else:
        for c in range(len(check)):
            if music_length == check[c][0]:
                return check[c][1]


def change_time(a, b):
    return int(a) * 60 + int(b)