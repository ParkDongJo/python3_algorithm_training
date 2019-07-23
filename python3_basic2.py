'''
파이썬 응용 자료형 (튜플은 우선 학습하지 않는다)
1. 리스트
2. 딕셔너리
'''

'''
1. 리스트

    list.index( value ) : 값을 이용하여 위치를 찾는 기능
    list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 (‘+’연산자 보다 성능이 좋음)
    list.insert( index, value ) : 원하는 위치에 값을 추가
    list.sort( ) : 값을 순서대로 정렬
    list.reverse( ) : 값을 역순으로 정렬
'''
list1 = []
list2 = [1,2]
list3 = [1,2,'a','b']
list4 = [1,2,['a','b']]

# 리스트 인덱싱
print(list4[0])
print(list4[-1])
print(list4[0] + list4[1])
print(list4[-1][0])

# 리스트 슬라이싱
print(list4[0:2])
print(list4[2:][0][0])

# 리스트 연산
print(list2 * 2)
print(len(list2))
print(str(list2[0]) + "hi")

# 리스트 수정/ 삭제
list4[2] = 4
print(list4)

del list4[2]
print(list4)

list5 = [1,2,3,4,5,6]
del list5[3:]
print(list5)

# 리스트 지원 내부함수
list5.append(6) # append(x)
list5.append(1)
print(list5)

list5.sort() # sort()
print(list5)
list5.reverse() # reverse()
print(list5)
print(list5.index(2)) # index(x)
list5.remove(3) # remove() 대입된 값의 첫번째 요소 삭제
list5.pop()  # pop()
print(list5)
print(list5.count(1)) # count(x)


'''
2. 딕셔너리
'''
dic2 = {1:'a'}
dic2[2] = 'b'
dic2['arr'] = [1,2]
print(dic2)

# 주의 사항
dic3 = {1: 'a', 1: 'b'}
print(dic3[1]) # 중복된 키값이 있을 시 하나를 제외한 나머진 무시됨
print('\n')

# 딕셔너리 지원 내부함수
dic4 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
for k in dic4.keys():
    print(k)

list7 = list(dic4.keys()) # keys()
print(list7)

print(dic4.values()) # values() - dic4 value들 값 dict_values()로 리턴

print(dic4.items()) # items() - dic4 key,value 쌍 얻기

dic3.clear() # clear()
print(dic3)
print(dic4.get(1)) # get(x)
print(2 in dic4) # x in list


'''
    파이썬 특수 컨테이너 타입 
    collection의 내장 메서드들
    * 자주 쓰이는 것에 표시해둠!!

    namedtuple() : factory function for creating tuple subclasses with named fields
    deque() : list-like container with fast appends and pops on either end
    ChainMap() : dict-like class for creating a single view of multiple mappings
    * Counter() : dict subclass for counting hashable objects
    * OrderedDict() : dict subclass that remembers the order entries were added
    defaultdict() : dict subclass that calls a factory function to supply missing values
    UserDict() : wrapper around dictionary objects for easier dict subclassing
    UserList() : wrapper around list objects for easier list subclassing
    UserString() : wrapper around string objects for easier string subclassing


'''