# 보이어 무어 법 (P.315)
# 7-3)
def bm_match(txt: str, pat: str) -> int:
    #건너뛰기 표 만들기
    skip = [None] * 256
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    #검색
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        print(pt)
        print(skip[ord(txt[pt])])
        print(len(pat)-pp)
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat)-pp else len(pat)-pp
        print(pt)

    return -1
