'''
[프로그래머스 정렬 문제]

문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	6210
[3, 30, 34, 5, 9]

'''

'''
    단순히 선택정렬을 활용해서 구현했다.
    하지만, 역시나 시간복잡도의 한계로 시간초과가 떴다..
    퀵정렬 또는 병합정렬로 코드를 개선해야한다.
    그래서 아래와 같이 병합정렬을 응용했다.
'''
def solution(numbers):
    answer = ''
    
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            s_prev = str(numbers[i])
            s_next = str(numbers[j])

            if s_prev[0] < s_next[0]:
                numbers[i], numbers[j] = swap(numbers[i], numbers[j])

            elif s_prev[0] == s_next[0]:
                if (s_prev + s_next) < (s_next + s_prev):
                   numbers[i], numbers[j] = swap(numbers[i], numbers[j])
    
    answer = ''.join(str(e) for e in numbers)

    return answer


'''
    시간 초과 실패 때문에 N(logN)의 속도인 병합정렬을 활용했다.
    그럼에도 불구하고 한개의 사간초과가 떴다. 우선 이는 병합정렬의 응용적인 부분에 있어서, 좀더 최적화를 하면 될것 같다
    두번째는 한개의 테스트 케이스가 실패했는데, 아무래도 [0,0,0] 같은 테스트 케이스 인것 같다
    우선 이건 패스하자!

    채점 결과
    Correctness: 81.8
    합계: 81.8 / 100.0
'''
'''
1. 동일한 숫자가 입력될 수 있다는 점
2. "0000" → "0" 으로 출력해야하는 점
'''

def another_solution(numbers):
    list = [str(e) for e in numbers]
    result = merge_sort(list)
    if result[0] == '0':
        return 0
    else:
        return ''.join(result)

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:

            if (left[0] + right[0]) < (right[0] + left[0]):
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


# print(solution([1, 31, 30, 3, 34, 54, 5, 9, 872]))
print(another_solution([1, 31, 30, 3, 34, 54, 5, 9, 872]))
print(another_solution([0,0,0]))
