# 괄호 변환

def is_right(u):  # 올바른 문자열인지 확인
    cnt_a = 0
    for i in u:
        if i == '(':
            cnt_a += 1
        else:
            cnt_a -= 1
        if cnt_a < 0:
            return False
    return True


def process(w):  # 재귀적으로 부르기 위해 모든 과정을 한 함수에 모음
    if w == "":
        return ""
    u = ''
    v = ''
    cnt_a = 0
    cnt_b = 0
    for i in w:
        u += i
        if i == '(':
            cnt_a += 1
        else:
            cnt_b += 1
        if cnt_a == cnt_b:
            break
    v = w[cnt_a + cnt_b:]
    print("u", u, "v", v)
    if chk_right(u):
        # 3-1
        u += process(v)
        return u
    else:
        # 4
        new = '('
        new += process(v)
        new += ')'
        print("u", u, "v", v)
        print("u", u)
        for j in u[1:-1]:  # [1:-1]은 1인덱스부터 마지막 인덱스 앞까지만 반복
            if j == '(':
                new += ')'
            else:
                new += '('
        return new


def solution(p):
    answer = process(p)

    return answer


p = input()

print(solution(p))
