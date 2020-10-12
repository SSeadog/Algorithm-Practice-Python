# 문자열 재정렬

# s 입력
S = list(input())

# S에서 나온 숫자와 문자열을 저장할 리스트
Str = []
Int = []

# S를 순차탐색
for s in S:
    # s가 int로 변환되지 않는다면 s는 문자열이므로 Str에 추가하고, 변환되면 Int에 추가
    try:
        Int.append(int(s))
    except:
        Str.append(s)

# Str을 정렬하고 하나씩 출력한 뒤 끝에 Int의 합을 붙여서 출력
for s in sorted(Str):
    print(s, end="")
print(sum(Int))
