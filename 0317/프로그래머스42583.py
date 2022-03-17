def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    complete = []
    time = 0
    long = len(truck_weights)
    while len(complete) < long:
        time += 1
        out = bridge.pop(0)
        if out != 0:
            complete.append(out)
        if len(truck_weights) > 0:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time