# 두 배열의 원소 교체

# N,K 입력
n, k = map(int, input().split())

# 배열A 입력
array_A = list(map(int, input().split()))

# 배열B 입력
array_B = list(map(int, input().split()))

# 배열A는 오름차순 정렬
array_A = sorted(array_A)
# 배열B는 내림차순 정렬
array_B = sorted(array_B, reverse=True)

# K번 바꿔치기
for i in range(k):
    array_A[i], array_B[i] = array_B[i], array_A[i]

# 결과 출력
print(sum(array_A))
