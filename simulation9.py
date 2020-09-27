# 뱀

from collections import deque


def solution():
    # 보드 크기, 사과 개수 입력
    n = int(input())
    k = int(input())

    # 보드 선언, 사과 위치 입력받고 위치시킴
    board = [[0] * n for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        board[y-1][x-1] = 2

    for i in range(n):
        print(board[i])

    # 방향 변환 횟수 l 입력
    l = int(input())

    # 방향 변환 정보 저장
    turn = deque()
    for _ in range(l):
        t, direction = input().split()
        if direction == 'D':
            direction = 1
        else:
            direction = -1
        turn.append((int(t), direction))

    # 진행 시간
    time = 0

    # 뱀의 위치와, 각 좌표를 저장할 큐
    q = deque()

    # q에 시작 위치 넣음
    q.append((0, 0))

    # 뱀의 현재 위치를 1로 바꿈
    board[0][0] = 1

    # 뱀의 머리 위치
    head = [0, 0]

    # 뱀의 형재 방향 저장 0,1,2,3 -> 북,동,남,서
    d = 1

    while True:
        time += 1
        # 뱀 머리 이동
        if d == 0:
            head[1] -= 1
        elif d == 1:
            head[0] += 1
        elif d == 2:
            head[1] += 1
        else:
            head[0] -= 1
        # 이동한 위치 큐에 넣음
        q.appendleft((head[0], head[1]))
        # 뱀의 머리가 보드 위치를 벗어나면 끝냄
        if head[0] >= n or head[0] < 0 or head[1] >= n or head[1] < 0:
            return time
        # 자기 몸을 만났다면 종료
        if board[head[1]][head[0]] == 1:
            return time
        # 사과를 먹지 않았다면 큐에서 맨 오른쪽 값을 빼고 보드 갱신
        if board[head[1]][head[0]] != 2:
            tail = q.pop()
            board[tail[1]][tail[0]] = 0

        # 뱀의 머리가 이동했으므로 보드 값 갱신
        board[head[1]][head[0]] = 1

        # 방향 전환이 필요하다면 turn에서 꺼내고 방향 전환
        if turn:
            if turn[0][0] == time:
                t = turn.popleft()[1]
                d += t
                if d == 4:
                    d = 0
                if d == -1:
                    d = 3


print(solution())
