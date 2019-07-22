'''
[프로그래머스 큐 문제]

'''
def solution(arrangement):
    answer = 0
    stack = []
    pipe_cnt = 0
    
    for curr in arrangement:
        if curr == '(':
            stack.append(curr)
            last = curr

        else:
            if last == '(':
                stack.pop()
                answer .+= len(stack)
                last = curr
            else:
                stack.pop()
                answer += 1             

    return answer


print(solution('()(((()())(())()))(())'))