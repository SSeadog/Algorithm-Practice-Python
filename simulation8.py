# 자물쇠와 열쇠

import numpy

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

n = 3  # key의 크기

print(key)

r_key = numpy.rot90(key, k=3, axes=(0, 1))  # 시계방향으로 90도 돌리기


def key_move(key, direction):
    if direction == 0:  # 오른쪽으로
        prev = [0] * n
        for i in range(n):
            for j in range(n):
                key[j][i], prev[j] = prev[j], key[j][i]


key_move(key, 0)
print(key)
