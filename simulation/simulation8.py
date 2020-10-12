# 자물쇠와 열쇠

import numpy


# r_key = numpy.rot90(key, k=3, axes=(0, 1))  # 시계방향으로 90도 돌리기


# lock을 크게 선언하고 키를 옮겨서 확인하는 식으로 이 함수는 필요 없음
# def key_move(key, direction):
#     if direction == 0:  # 오른쪽으로
#         prev = [0] * m
#         for i in range(m):
#             for j in range(m):
#                 key[j][i], prev[j] = prev[j], key[j][i]


def chk(new_lock):
    n = len(new_lock) // 3
    for i in range(n):
        for j in range(n):
            if new_lock[i + n][j + n] != 1:
                return False
    return True


def solution():
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

    # lock을 3배의 크기로 선언하고 값 넣기
    new_lock = [[0] * (len(lock) * 3) for _ in range(len(lock) * 3)]
    for i in range(len(lock), len(lock) * 2):
        for j in range(len(lock), len(lock) * 2):
            new_lock[i][j] = lock[i-len(lock)][j-len(lock)]

    n = len(lock)
    m = len(key)

    # 90도씩 돌리기
    for _ in range(4):
        new_lock = numpy.rot90(new_lock, k=3, axes=(0, 1))

        # key를 옮기며 new_lock에 더하고 확인하고 빼기
        for x in range(1, n * 2):
            for y in range(1, n * 2):
                # new_lock에 key 더하기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 체크
                if chk(new_lock):
                    return True
                # key 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    # 4회전 모두 확인하고 이 부분에 도달했다면, 키가 맞지 않는다는 의미이므로 False리턴
    return False


print(solution())
