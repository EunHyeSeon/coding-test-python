def solution(weights):
    answer = 0
    weight_dict = {}
    for w in weights:
        weight_dict[w] = weight_dict.get(w, 0) + 1
    for w in weights:
        if w % 2 == 0:
            answer += weight_dict.get(w*3//2, 0)
        if w % 3 ==0:
            answer += weight_dict.get(w*4//3, 0)
        answer += weight_dict.get(w*2, 0)
    for w in weights:
        weight_dict[w] -= 1
        answer += weight_dict[w]
    return answer
