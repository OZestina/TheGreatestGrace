# 브루트 포스법, brute force method (P.305)
# 문자열에서 부분 문자열 검색 알고리즘

# 7-1) 브루트 포스법으로 문자열 검색하기
def bf_match(txt: str, pat: str) -> int:
    pt = 0  #txt 커서
    pp = 0  #pat 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트 입력: ')
    s2 = input('패턴 입력: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 없습니다')
    else:
        print(f'{(idx+1)}번째 문자에 패턴이 나옵니다')
        
