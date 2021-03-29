n = 3
k = 3

def solution(n, k):
    def factorial(n):
        result = 1
        for i in range(2,n+1):
            result*=i
        return result

    answer = []
    arr = [i for i in range(1,n+1)]
    k -= 1
    for i in reversed(range(1,n)):
        m = k // factorial(i)
        k = k % factorial(i)
        answer.append(arr[m])
        arr.pop(m)
        print(answer,arr)
    answer.append(arr.pop())
    return answer