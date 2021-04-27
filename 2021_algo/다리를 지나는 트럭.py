def solution(bridge_length, weight, truck_weights):
    bridge_sum = 0
    bridge_count = 0
    
    time = 0
    while truck_weights:
        x = truck_weights[0]
        if bridge_count <= bridge_length:
            if bridge_sum + x <= weight:
                bridge_count += 1
    return time