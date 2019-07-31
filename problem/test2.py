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

kNumToNum = {
    0:'영',
    1:'일',
    2:'이',
    3:'삼',
    4:'사',
    5:'오',
    6:'육',
    7:'칠',
    8:'팔',
    9:'구',
}

def solution(aStr, bStr):
    aList = [char for char in aStr]
    bList = [char for char in bStr]

    aBigNum = convertStrToNum(aList)
    bBigNum = convertStrToNum(bList)

    print(aBigNum)
    print(bBigNum)
    sum = aBigNum + bBigNum
    print(sum)

    return convertNumToStr(sum)
        
        

def convertStrToNum(numStrList):
    tmpList = []

    for idx, c in enumerate(numStrList):
        num = kNumSys[c]
        if c == '만' or c == '억' or c == '조':
            tmpList.append(num)
        else:
            tmpList.append(num)
        
    c = 1
    tmp = 0
    result = 0
    for num in tmpList:
        if num < 10:
            c = num
        elif num >= 10 and num <= 1000:
            tmp += c * num
            c = 1
        else:
            if c != 1 and tmp == 0:
                result += c * num
                c = 1
            else:
                if c != 1:
                    tmp += c
                    c = 1
                result += tmp * num
                tmp = 0

    if c is not 1:
        result += tmp + c


    return result


def convertNumToStr(bigNum):
    result = ''
    num = bigNum // 1000000000000
    result += parseUnit(num) + '조'
    bigNum -= num * 1000000000000

    num = bigNum // 100000000
    result += parseUnit(num) + '억'
    bigNum -= num * 100000000

    num = bigNum // 10000
    result += parseUnit(num) + '만'
    bigNum -= num * 10000
    print(bigNum)

    num = bigNum
    result += parseUnit(num)
    
    return result

def parseUnit(num):
    str = ''
    if num // 1000 > 0:
        str += kNumToNum[num // 1000] + '천'
        num -= (num//1000) * 1000
    if num // 100 > 0:
        str += kNumToNum[num // 100] + '백'
        num -= (num//100) * 100
    if num / 10 > 0:
        str += kNumToNum[num // 10] + '십'
        num -= (num//10) * 10
    if num > 0:
        str += kNumToNum[num]
    # print(str)

    return str

# 삼십이조 팔천팔백팔십팔억 칠천구백팔십육만 칠천사백삼십팔
# '삼십이조 팔천팔백팔십팔억 칠천구백팔십육만 칠천사백삼십팔'
print(solution('삼조칠천팔백육십이억삼천사백삼십구', '이십구조천이십육억칠천구백팔십육만삼천구백구십구'))
    