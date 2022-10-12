# https://school.programmers.co.kr/learn/courses/30/lessons/17677

# 1st try
# set을 사용하면 중복된 내용이 사라져서 다른 방식으로 풀었는데
# 다른 사람의 풀이를 보니 set으로 진행하고 합/교의 내용을 기반으로 개수를 세는 방식이 있었다 (교집합은 min값으로, 합집합은 max값으로)
# 사실 결국에는 교집합의 개수와 합집합의 개수만 필요하니까 해당 방법이 더 적은 시간이 들듯..!
def solution(str1, str2):
    #lower alphabet
    str1 = str1.lower()
    str2 = str2.lower()
    
    #two letter without num & special symbols
    arr1 = sorted([str1[i:i+2] for i in range(len(str1)-1) if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z'])
    arr2 = sorted([str2[i:i+2] for i in range(len(str2)-1) if 'a' <= str2[i] <= 'z' and 'a' <= str2[i+1] <= 'z'])
    
    #end for empty set
    if len(arr1) == 0 and len(arr2) == 0: return 65536
    if len(arr1) == 0 or len(arr2) == 0: return 0
    
    #intersection
    inter = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            inter.append(arr1[i])
            i += 1
            j += 1
        else:
            if arr1[i] < arr2[j]: i += 1
            else: j += 1
    #union
    union = arr1 + arr2
    for pair in inter:
        union.remove(pair)
    
    return int(65536 * len(inter) / len(union))
  
