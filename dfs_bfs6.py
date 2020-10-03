# 괄호 변환

# 1,2번에 해당하는 함수
def split(w):
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
    v = w[cnt_a + cnt_b + 1:]
    return u, v

# 올바른 문자열인지 확인


def chk_right(u):
    cnt_a = 0
    for i in w:
        if i == "(":
            cnt_a += 1
        else:
            cnt_a -= 1
        if cnt_a < 0:
            return False
    return True


def solution(p):
    answer = ''
    u, v = split(p)

    # 3번부터 만들면 됨
    return answer


p = input()

solution(p)
