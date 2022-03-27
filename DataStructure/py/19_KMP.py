# KMP법 (P.310)
# 검사한 결과를 다시 활용하는 str in str 검색 알고리즘

# 7-2) KMP법으로 문자열 검색
def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)
    
    #건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
            
    #문자열 작성
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트 입력: ')
    s2 = input('패턴 입력: ')
    
    idx = kmp_match(s1, s2)
    
    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다')
    else:
        print(f'{(idx+1)}반째 문자가 일치합니다')
