'''
[프로그래머스 큐 문제]

'''

import heapq

def solution(priorities, location):
    heap = []
    queue = []

    for val in priorities:
        heapq.heappush(heap, (-val, val))  # (우선 순위, 값)

    for idx, val in enumerate(priorities):
        queue.append({'tag': True if idx == location else False,
                     'val': val})

    answer = 0
    length = len(queue)
    while 0 != len(queue):
        curr = queue[0]
        top = heap[0]

        if curr['val'] == top[1]:
            queue.pop(0)
            heapq.heappop(heap)
            answer += 1

            if curr['tag']:
                break
        else:
            queue.pop(0)
            queue.append(curr)
        
    return answer


'''
    다른 이들의 더 좋은 해법
'''
def another_solution(priorities, location):
    answer = 0
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
        else :
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else :
                location -= 1
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))