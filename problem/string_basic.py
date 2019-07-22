'''
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.

입출력 예
s	    return
a234	false
1234	true
'''
def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if (48 <= ord(c) and  57 >= ord(c)) is not True:
                answer = False
                break
    else:
        answer = False

    return answer

print(solution("0234"))


# 베스트 답안
def another_solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


def another_solution2(s):
    number_str = len(s)
    try:
        float(s)
        if number_str == 4 or number_str == 6:
            return True
        else:
            return False
    except ValueError:
        return False