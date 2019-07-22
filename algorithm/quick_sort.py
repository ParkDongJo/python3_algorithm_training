'''
    퀵정렬
    - 시간복잡도 : N * logN

    - fivot을 기준으로 fivot보다 큰값과 작은값을 교체
    - 왼쪽부터 fivot보다 큰값 찾기
    - 오른쪽부터 fivot보다 작은값 찾기
    - 각각 찾았을 시 두 값의 위치를 교체해준다.
    - 계속 반복
    - 서로 엇갈렸을 시에는 fivot값과 오른쪽부터 찾은 작은값의 위치를 교체해준다.
    - 이와같은 행위를 재귀적으로 실행한다.
'''
g_array = [2,4,1,6,9,12,8,7]
def quick_sort(start, end):
    if(start >= end): 
        return
    pivot, i, j, tmp = start, start+1, end, 0

    while i <= j:   # 엇갈릴 때 까지 반복한다.
        while i <= end and g_array[i] <= g_array[pivot]: i += 1
        while j > start and g_array[j] >= g_array[pivot]: j -= 1
        
        if i > j:
            g_array[pivot],g_array[j] = swap(g_array[pivot], g_array[j])
        else:
            g_array[i], g_array[j] = swap(g_array[i], g_array[j])
    
    quick_sort(start, j-1)
    quick_sort(j+1, end)
    
def swap(s1, s2):
    return s2, s1


quick_sort(0, len(g_array)-1)
print(g_array)


'''
    더 깔끔한 방법
    아래의 코드는 위에 코드보다 훨씬 간결하고 직관적이다.
    물론 효율적인 면에서는 내부적으로 여러개의 배열을 생성 후 합치고 하기때문에,
    메모리 효율은 떨어질 수 있겠으나, 코드의 간결함이 너무 매력적이다.
'''
def another_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    left,right,equal =[],[],[]

    for a in array:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    return another_quick_sort(left) + equal + another_quick_sort(right)


print(another_quick_sort([2,4,1,6,9,12,8,7]))