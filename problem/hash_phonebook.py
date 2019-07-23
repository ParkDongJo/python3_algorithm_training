
'''
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
입출력 예제
phone_book	return
[119, 97674223, 1195524421]	false
[123,456,789]	true
[12,123,1235,567,88]	false
입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

알림

2019년 5월 13일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.
'''
TABLE_SIZE = 10000

class HashTable():
    def __init__(self, size=TABLE_SIZE):
        self.table = [[] for _ in range(TABLE_SIZE)]

    def set(self, num):
        list, key2 = self.find(num)
        list.append(num)
    

    def get(self, num):
        list, key2 = self.find(num)

        if len(list) == 0:
            return False
        else:
            return list[key2]


    def find(self, num):
        key1 = num % TABLE_SIZE
        list = self.table[key1]

        if len(list) != 0:
            for key2 in range(0, len(list)):
                if list[key2] == num:
                    return list, key2

        return list, -1


def solution(phone_book):
    hash_table = HashTable()
    phone_book.sort()

    for num in phone_book:
        str_num = ''
        for e in num:
            str_num += e
            if hash_table.get(int(str_num)) is not False:
                return False
        hash_table.set(int(num))

    return True

# print(solution(['119', '97674223', '1195524421']))
# print(solution(['123','456','789']))
# print(solution(['12','123','1235','567','88']))



'''
    다른 사람 풀이
'''
def another_solution1(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


'''
    다른 사람 풀이
'''
def another_solution2(phoneBook):
    phoneBook.sort()
    a= len(phoneBook[0])
    arr = list()
    for i in range(len(phoneBook)):
        arr.append(phoneBook[i][0:a])
    for j in range(len(phoneBook)-1):
        if arr[0] == arr[j+1]:
            answer = False
            break
        else:
            answer = True
    return answer

print(another_solution2(['119', '97674223', '1195524421']))
print(another_solution2(['123','456','789']))
print(another_solution2(['12','123','1235','567','88']))