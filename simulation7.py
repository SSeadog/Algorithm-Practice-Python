# 문자열 압축

# s 입력
s = input()

# 1,2,3'''만큼 자른 s를 저장할 split 리스트 선언
split = [[] for _ in range(int(len(s)/2) + 1)]
# size만큼 자르고 split[size]에 저장
for size in range(1, int(len(s)/2) + 1):
    for i in range(0, len(s), size):
        split[size].append(s[i:i+size])
# 압축한 문자열의 개수를 저장할 리스트
result = []

# 자를 크기를 변경하며 반복
for i in range(1, len(split)):
    # i단위로 문자열을 자른 리스트를 s에 넣음
    s = split[i]
    # 중간 값을 저장할 변수 선언
    temp_result = ""
    temp_cnt = 1
    # 첫 항을 prev에 넣음
    prev = s[0]
    # 두 번째항부터 prev와 비교하며 같다면 cnt + 1, 다르면 temp_result에 추가해줌
    for j in range(1, len(s)):
        if prev == s[j]:
            temp_cnt += 1
        else:
            if temp_cnt > 1:
                temp_result += str(temp_cnt)
                temp_cnt = 1
            temp_result += prev
        prev = s[j]
    # 마지막 항을 계산함
    if temp_cnt > 1:
        temp_result += str(temp_cnt)
        temp_cnt = 1
    temp_result += s[-1]

    # 압축된 문자열의 길이를 result에 추가함
    result.append(len(temp_result))
# 최소 출력
print(min(result))


# # 문자열을 이상하게 다룸. size만큼 1개면 1개씩 2개면 2개씩 저장해서 비교하는 게 편할 듯

# # s 입력
# s = list(input())

# # 잘린 결과를 저장할 배열
# result = [len(s)] * (int(len(s)/2)+1)

# # size 단위 만큼 자르며, N/2 만큼 반복
# for size in range(1, int(len(s)/2)+1):
#     # size로 자르며 중간 결과를 저장할 변수들
#     temp_result = ""
#     temp_str = ""
#     temp_cnt = 1
#     # s를 순차탐색한 size 단위로
#     for i in range(0, len(s)-size+1, size):
#         # 현재 문자열
#         cur = ""
#         for j in range(i, i+size):
#             cur += s[j]
#         # 다음 문자열
#         nex = ""
#         if i+size+size <= len(s):
#             for j in range(i+size, i+size+size):
#                 nex += s[j]
#         # 현재 값과 다음 값이 같다면 cnt + 1
#         if cur == nex:
#             temp_cnt += 1
#         # 다르다면 temp_str에 현재 문자열을 넣고
#         else:
#             temp_str = cur
#             # cnt가 1보다 크다면 temp_result에 추가, cnt 초기화
#             if temp_cnt > 1:
#                 temp_result += str(temp_cnt)
#                 temp_cnt = 1
#             # temp_str을 temp_result에 추가
#             temp_result += temp_str
#     print(temp_result)
#     result[size] = len(temp_result)
# print(result)
