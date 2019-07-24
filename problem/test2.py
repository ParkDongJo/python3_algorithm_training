kNumSys = {
    '영': 0,
    '일': 1,
    '이': 2,
    '삼': 3,
    '사': 4,
    '오': 5,
    '육': 6,
    '칠': 7,
    '팔': 8,
    '구': 9,
    '십': 10,
    '백': 100,
    '천': 1000,
    '만': 10000,
    '억': 100000000,
    '조': 1000000000000
}

def solution(aStr, bStr):
    aList = [char for char in aStr]
    bList = [char for char in bStr]
    result = 0

    print(aList)
    print(bList)
    for c in aList:
        num = kNumSys[c]
        if num > 9:
            result += tmp * num
        else:
            tmp = num
        
    print(result)


print(solution('삼조칠천팔백육십이억삼천사백삼십구', '이십구조천이십육억칠천구백팔십육만삼천구백구십구'))
    