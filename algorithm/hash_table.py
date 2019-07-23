'''
    해시
    - 데이터를 최대한 빠른 속도로 관리하도록 도와주는 자료구조
    - 해시를 사용하면 메모리 공간이 많이 소모되지만 매우 빠른 속도로 데이터를 처리
    - 빠르게 데이터에 접근할 수 있다는 점에서 데이터 베이스 등의 소프트웨어에서 사용된다.

    - 특정한 값을 찾고자 할때 해당 key로 접근 할수 있다. 일반적으로 해시 함수는 모듈로(Modulo)연산등의
      수학적 연산으로 이루어져 있으므로 O(1)만에 값에 접근할 수 있다.

    - 해싱알고리즘은 나눗셈법이 자주 활용된다.
    - 충돌에 대한 대비로
        1) 충돌을 발생시키는 항목을 해시 테이블의 다른 위치에 저장 : 선형조사법, 이차조사법
        2) 해시 테이블의 하나의 버켓에 여러개의 항목 저장 : 체이닝
'''
from random import *

TABLE_SIZE = 10007
INPUT_SIZE = 5000

class Hashtable: 
    def __init__(self): 
        self.table = [None for _ in range(TABLE_SIZE)] 
    
    # 해시 함수
    def simple_hash(self, name): 
        sum = 0 
        for letter in name: 
            sum += ord(letter) # print(name, sum, sum % len(self.table)) 
        return sum % len(self.table) 
        
    # 해시 테이블에 데이터 입력
    def put(self, name, num): 
        self.table[self.simple_hash(name)] = num 
        
    # 테이블의 모든 데이터 출력
    def show(self):
        for idx, value in enumerate(self.table): 
            if value is not None:
                print(idx, value)

    # 특정 데이터 가져오기       
    def find(self, name): 
        return self.table[self.simple_hash(name)]

'''
    선형조사법의 단점

    선형 조사법은 충돌이 발생하기 시작하면, 유사한 값을 가지는 데이터끼리
    서로 밀집되는 집중 결합 문제가 존재한다.

    물론 선형조사법이라고 해도 '해시 테이블의 크기'가 비약적으로 크다면,
    다시 말해 메모리를 많이 소모한다면 충돌이 적게 발생하므로 매우 빠른
    데이터 접근 속도를 가질 수 있습니다.

    > 단점 보완을 위해 이차조사법을 사용!!
    완전 제곱수로 키값을 늘려가는 기법
'''

'''
    체이닝 기법

    체이닝 기법은 연결리스트를 활용해 특정한 키를 가지는 항목들을 연결하여 저장합니다.
    연결 리스트를 사용한다는 점에서 삽입과 삭제가 용이합니다. 또한 테이블 크기 재설정 문제는
    '동적 할당'을 통해서 손쉽게 해결할 수 있습니다. 다만 동적 할당을 위한 추가적인 메모리 공간이
    소모된다는 단점이 있습니다.
'''

'''
해시테이블 (체이닝)
    체이닝 방식으로 구현하기
    오픈어드레싱 방식으로 구현하기 (선택)
    unittest를 통해 구현체에 대한 검증 (push, pop, peek, (array 기반인 경우) expand, 저장되지 않은 값의 참조 등)
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTableChaining():

    def __init__(self, size=7):
        self.table = [[] for _ in range(size)]
        self.size = size

    def set(self, key, value):
        new_node = Node(key, value)
        box, item, in_index = self.find(key)
    
        if item is None:
            box.append(new_node)
        else:
            item = new_node


    def get(self, key):
        _, item, in_index = self.find(key)
        if item is None:
            return None

        return item.value


    def delete(self, key):
        box, item, in_index = self.find(key)
        if item is None:
            return False
    
        del_item = box.pop(in_index)
        return del_item.value


    def find(self, key):
        hash_key = hash(key)
        index = hash_key % self.size

        box = self.table[index]
        
        for in_index in range(0, len(box)):
            item = box[in_index]
            if item.key == key:
                return box, item, in_index 

        return box, None, -1


hash_table = HashTableChaining()
        
