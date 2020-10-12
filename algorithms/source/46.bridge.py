def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 1
    bridge = []
    answer = 0
    while 1:
        answer += 1

        for i in range(0, len(bridge)):
            if bridge[i][1] >= bridge_length:
                bridge.pop(0)
                break
        if not bridge and not truck_weights:
            break
        elif not bridge:
            bridge.append(list((truck_weights.pop(0), time)))
        else:
            sum_wight = 0
            for i in range(0, len(bridge)):
                sum_wight += bridge[i][0]
            if not truck_weights:
                bridge[i][1] += 1
            elif truck_weights:
                while weight >= sum_wight + truck_weights[0]:
                    sum_wight += truck_weights[0]
                    bridge.append(list((truck_weights.pop(0), time)))
                    if not truck_weights:
                        break
                for i in range(0, len(bridge)):
                    bridge[i][1] += 1
            else:
                for i in range(0, len(bridge)):
                    bridge[i][1] += 1
    return answer


def solution2(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution2(bridge_length, weight, truck_weights))
