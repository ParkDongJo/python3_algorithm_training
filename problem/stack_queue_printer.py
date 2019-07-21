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
    count = 1
    length = len(queue)
    while 0 != len(queue):
        curr = queue[0]
        top = heap[0]

        if curr['val'] == top[1]:
            queue.pop(0)
            heapq.heappop(heap)
            if curr['tag']:
                answer
                break
        else:
            queue.pop(0)
            queue.append(curr)

        count += 1
        


    return answer


print(solution([2, 1, 3, 2], 2))