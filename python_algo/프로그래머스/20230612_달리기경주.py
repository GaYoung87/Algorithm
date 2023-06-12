def solution(players, callings):
    player_dict = {players[i]: i for i in range(len(players))}
    rank_dict = {i: players[i] for i in range(len(players))}

    for call in callings:
        now_idx = player_dict[call]

        now_player = call
        front_player = rank_dict[now_idx - 1]

        player_dict[now_player], player_dict[front_player] = now_idx-1, now_idx
        rank_dict[now_idx], rank_dict[now_idx - 1] = front_player, now_player

    return list(rank_dict.values())

# 시간초과 -> 50000 * 1000000는 시간초과
# def solution(players, callings):

#     for call in callings:
#         for i in range(len(players)):
#             if call == players[i]:
#                 temp = players[i-1]
#                 players[i-1] = players[i]
#                 players[i] = temp

#     return players