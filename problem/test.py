import sys

def solution(a, b):
    aBigNum, bBigNum = str(a), str(b)
    maxLen = max(len(aBigNum), len(bBigNum))
    aChar = attachZero(aBigNum, maxLen)
    bChar = attachZero(bBigNum, maxLen)

    answer = addBigNum(aChar, bChar)

    for c in answer:
        sys.stdout.write(c)

def addBigNum(aChar, bChar):
    result = []
    carry = 0
    
    for i in range(len(aChar)-1, -1, -1):
        tmp = (ord(aChar[i]) - 48) + (ord(bChar[i])-48) + carry

        if tmp > 9:
            result.insert(0, str(tmp % 10))
            carry = 1
        else:
            result.insert(0, str(tmp))
            carry = 0

    return result


def attachZero(numStr, maxLen):
    while len(numStr) <  maxLen:
        numStr = "0" + numStr

    return [char for char in numStr]


solution(123112981293812938139, 1298928491101221811)