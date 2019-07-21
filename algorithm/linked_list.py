'''
    추상적 자료구조

    연결 리스트
    - 삽입, 삭제, 순회...
    - 정렬, 탐색...

    Node class
    - Data
    - Link(next)

    LinkedList class
    - Head : list의 가장 앞 노드
    - Tail : list의 가장 끝 노드
    - total : 노드의 총 갯수
    - idx는 1부터 시작하게 하고, 0은 다른 목적으로 쓴다(구현이 훨씬 쉬울수 있다)

    - 길이 얻어내기
    - 리스트 순회
    - 특정 원소 참조
    - 원소삽입
    - 원소삭제
    - 두리스트 합치기
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.total = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def getAt(self, pos):
        if pos <= 0 or pos > self.total:
            return None

        i = 0
        curr = self.head
        while i<pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        list = []
        curr = self.head
        while curr.next:
            curr = curr.next
            list.append(curr.data)

        return list
            
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.total +1:
            return False
    
        if pos != 1 and pos == self.total +1:
            prev = self.tail
        
        else:
            prev = self.getAt(pos-1)
        
        return self.insertAfter(prev, newNode)


    def popAt(self, pos):
        if pos < 1 or pos > self.total +1:
            return False

        curr = self.getAt(pos)

        if curr == self.head:
            if curr.next != None:
                self.head = curr.next
                curr.next = None
            
            else:
                self.head = None
            
        
        elif curr == self.tail:
            prev = self.getAt(pos-1)
            self.tail = prev
            prev.next = None

        else:
            prev = self.getAt(pos-1)
            prev.next = self.getAt(pos).next

        self.total -= 1


        # 맨앞의 node를 삭제할 때
        # prev 없음
        # Head 조정필요

        # 맨끝의 node를 삭제할때

        # 유일한 노드 삭제할 때

    def concat(self, list):
        self.tail.next = list.head.next

        if list.tail:
            self.tail = list.tail

        self.total += list.total


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next

        if prev.next is None:
            self.tail = newNode

        self.total += 1
        return True


    def popAfter(self, prev):


'''

                배열    vs   연결리스트
저장공간        연속한 위치  / 임의의 위치
특정원소        지칭 매우간편 / 선형탐색과 유사
시간 복잡도      O(1)      / O(n)


    연결리스트 장점
    - 삽입과 삭제가 유연하다
    - insertAfter(prev, newNode) <- 맨앞은 어떻게
    - popAfter(prev) <- 맨뒤는 어떻게
    - head를 dummy node로 바꾼다.

'''
'''
    원소삽입의 시간 복잡도
    - 맨앞에 삽입하는 경우 O(1)
    - 중간에 삽입하는 경우 O(n)
    - 맨끝에 삽입하는 경우 O(1)
'''
'''
    원소섹제의 시간 복잡도
    - 맨앞에 삭제하는 경우 O(1)
    - 중간에 삭제하는 경우 O(n)
    - 맨끝에 삭제하는 경우 O(n)
'''