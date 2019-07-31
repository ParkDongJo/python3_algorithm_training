'''
    [중복제거 문제] - 셀프문제
    중복된 수가 들어가 있는 배열이 주어지면, 중복을 제거한 수의 배열을
    리턴하는 함수를 만들자

    [예시]
    입력
    [1,2,2,3]
    출력
    [1,2,3]


    [핵심 키워드]
    - 새로운 배열
    - 중복여부 확인
'''

def solution(list):

    unique_list = []
    for i in range(0, len(list)):
        is_pass = True
        num = list[i]

        for j in range(0, len(unique_list)):
            if num == unique_list[j]:
                is_pass = False
                break
            
        if is_pass:
            unique_list.append(num)
                
    return unique_list


print(solution([6,1,2,2,3,3,2,4,4,6]))
        
                    