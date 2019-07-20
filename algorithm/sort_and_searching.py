'''
    정렬과 탐색에 대해서 내용 정리
'''

'''
    python 리스트 정렬  
    - sorted(list)  : 정렬된 새로운 리스트를 얻어냄
    - list.sort() : 해당 리스트를 정렬함

    - sorted(list, reverse=True)
    - list.reverse()  or list.sort(reverse=True)
'''

'''
    문자열 정렬
     - sorted() 정렬에 이용하는 key를 지정
     - sort() 정렬에 이용하는 key를 지정
'''
str_list = ['abcd', 'xyz', 'spamd']
print(sorted(str_list, key=lambda x: len(x)))

dic_list = [{'name': 'Xohn','score':70}, {'name': 'Paul', 'score': 90}]
dic_list.sort(key=lambda x:x['name'])
print(dic_list)
dic_list.sort(key=lambda x:x['score'], reverse=True)
print(dic_list)
print('\n')

'''
    탐색 알고리즘 1
    - 선형탐색 (linear search)
    - 시간복잡도 O(n)
'''
L = [ 2, 10, 4, 5, 8 , 3, 9]
def linear_search(list, x):
    i=0
    while i < len(list) and list[i] != x:
        i += 1
    
    if i < len(list):
            return i
    else:
        return -1

print(linear_search(L, 5))
print(L.index(5))


'''
    탐색 알고리즘 1
    - 이진탐색 (binary search)
    - divide & conquer = 한번 비교가 일어날 때마다 리스트 반씩 줄임
    - 시간복잡도 O(log n)

    - lower , middle, upper를 설정
    - middle = (lower + upper) // 2
    - middle 이 찾고자하는 값보다 작으면 middle 왼쪽 배열 값을 무시하고 lower을 그 다음 배열인덱스 값을 가르키도록 한다
    - middle 이 찾고자하는 값보다 크면 middle 오른쪽 배열 값을 무시하고 upper을 그 전의 배열인덱스 값을 가르키도록 한다
    - 값을 찾을 때 까지 반복한다.
'''
def binary_search(list, target):
    lower = 0
    upper = len(list) -1
    idx = -1

    while lower <= upper:
        middle = (lower + upper) // 2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1

    return -1

print(binary_search(L, 6))
print(binary_search(L, 5))
