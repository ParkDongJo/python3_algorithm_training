'''
    재귀 알고리즘
    - 하나의 함수에서 자기 자신을 다시 호출
    - 많은 문제가 재귀적으로 문제 해결 가능 ( ex> 이진트리 , 자연수의 함 구하기)
    - 모든 재귀는 반복문으로 작성될수 있다.

    [작성 원리]
    - 종결조건을 작성한다
    - 그게 아니라면 재귀적으로 호출한다
'''
# 재귀 버전 - 시간복잡또 O(n) / 함수를 호출하기 때문에 효율성은 떨어짐
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

a = int(input("Number: "))
print(sum(a))

# 반복 버전 - 시간복잡도 O(n)
def loop_sum(n):
    sum = 0
    while n >= 0:
        sum += n
        n -= 1
    
    return sum

print(loop_sum(a))


'''
    재귀 알고리즘 응용
    - 조합의 수 (n개의 서로 다른 원소에서 m개를 택하는 경우의 수)
        ( n m ) = n! / m! * (n-m)!

        nC0 = 1, nCn = 1
        ( n m ) = ( n-1 m-1 ) + ( n-1 m ) / 포함하는 경우 + 포함하지 않은 경우
    - 하노이의 탑
'''
# 두번의 재귀 호출 -> 비효율적
def combi(n, m):
    if n == m:  # 골라내려는 것이 n(전체)와 같다면
        return 1
    elif m == 0: # 골라내려는 것이 0(아예) 없다면
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)

# 피보나치 F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2 (n>=2)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

# 피보나치 + 메모제이션
memo = {1:1, 2:1}
def fibo_memo(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]

fibo_memo(3)
print(memo)

# 피보나치 + Fast Multiplication
def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b