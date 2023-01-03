# 

# 1st try => 시간초과
# 문자열로 모두 바꿔서 세보려고 했으나 예상대로 실패
def cantor(n, arr):
    for i in range(n):
        temp = ''
        for n in arr[i]:
            if n == "1":
                temp += "11011"
            else:
                temp += "00000"
        arr.append(temp)
        
def solution(n, l, r):
    arr = ["1"]
    cantor(n, arr)
    return arr[-1][l-1 : r].count('1')
  
  
# 2nd try => 실패 어디서 잘못됐으려나
def count_one(n, l, r):
    answer = 0
    
    if n == 1:
        return "11011"[l-1 : r].count('1')
    if n == 2:
        return "1101111011000001101111011"[l-1 : r].count('1')
    
    how_big = 5 ** (n - 1)
    for i in range(5):
        if i == 2:  # 가운데 토막(0)인 경우 패스
            continue
    
        s, e = how_big * i + 1, how_big * (i + 1)
        print(n, l, ":", s, "/", r, ":", e)
        if l > e or r < s:      # 범위 해당 안되는 경우 패스
            print("pass")
            continue
        elif l <= s and e <= r:   # 범위 모두 포함 -> 가능한 모든 1의 개수
            answer += 4 ** (n - 1)
            print("all", answer)
        else:
            new_l = (max(l, s) - 1) % 5 + 1
            new_r = (min(r, e) - 1) % 5 + 1
            answer += count_one(n - 1, new_l, new_r)
            print(new_l, new_r, answer)
    return answer

def solution(n, l, r):
    answer = count_one(n, l, r)
    
    return answer
