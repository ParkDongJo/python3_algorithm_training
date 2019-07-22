'''
    병합정렬(merge sort)
    - 시간복잡도 : N * logN

    - 원소가 하나가 될 때까지 merge_sort()로 계속 잘게 쪼갠다.
    - 중심 원소를 기준으로 leftList와 rightList로 나눈다.
    - 원소가 하나가 될 때, merge()를 시작한다.
'''

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
    while len(left) > 0 or len(right) > 0: # 두 배열의 길이가 1이상 일때 반복문이 계속 돈다.
        if len(left) > 0 and len(right) > 0: # 두 배열의 길이가 모두 1이상 일때
            if left[0] <= right[0]:         # 왼쪽 배열의 첫번째 값이 오른쪽 배열 첫번째 값보다 작거나 같을 때 (=왼쪽이 작은 수 일때)
                result.append(left[0])
                left = left[1:]
            else:                           # 왼쪽 배열의 첫번째 값이 오른쪽 배열 첫번째 값보다 (=오른쪽이 작은 수 일때)
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:                 # 왼쪽 배열의 길이가 1이상일 때 (= 왼쪽 배열만 1개 이상일때 / 끝작업)
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:                # 오른쪽 배열의 길이가 1이상일 때 (= 오른쪽 배열만 1개 이상일때 / 끝작업)
            result.append(right[0])
            right = right[1:]
    return result