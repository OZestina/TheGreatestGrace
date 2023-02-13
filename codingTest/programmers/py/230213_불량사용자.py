# https://school.programmers.co.kr/learn/courses/30/lessons/64064


# 1st try
def cover_id(ban, user):
    for i in range(len(ban)):
        if ban[i] != '*' and ban[i] != user[i]:
            return 0
    return 1
    

def psb_pair(psb_id, ids, idx, maxi, stack):
    if idx == maxi:
        a = sorted(ids)
        if a not in stack:
            stack.append(a)
        return
    
    for i in psb_id[idx]:
        if i not in ids:
            ids[idx] = i
            psb_pair(psb_id, ids, idx + 1, maxi, stack)
            ids[idx] = -1
    
    
def solution(user_id, banned_id):
    l = len(banned_id)
    psb_id = []
    for b in range(l):
        l_b = len(banned_id[b])
        temp = []
        for u in range(len(user_id)):
            l_u = len(user_id[u])
            if l_b == l_u:
                if cover_id(banned_id[b], user_id[u]):
                    temp.append(u)
        if len(temp) == 0:
            return 0
        psb_id.append(temp)
    
    temp = [-1 for _ in range(l)]
    stack = []
    psb_pair(psb_id, temp, 0, l, stack)
    answer = len(stack)
    
    return answer
  

# 다른 사람의 풀이
# 중복되는 banned_id를 카운트해서 combination을 진행하면 재귀없이 빠르게 진행할 수 있다
# frozenset()은 값이 변하지 않는다 (tuple + set 성질) => hashable해서 set()에 담을 수 있다
from itertools import combinations

# 쿼리 (banned) 에 해당하는 id 들 리스트로 return
def find_banned_list(user_id, banned):
    result = []
    for id in user_id:
        if len(id) == len(banned):
            not_equal = False
            for i in range(len(id)):
                if banned[i] != "*" and id[i] != banned[i]:
                    not_equal = True
                    break
            if not not_equal:
                result.append(id)
    return result

def solution(user_id, banned_id):
    banned_list = dict()  # 각 쿼리에 대해서 해당하는 id 담는 곳
    count_banned_list = dict()  # 각 쿼리가 몇 번 나오는지 체크하는 곳
    for banned in banned_id:
        if banned not in count_banned_list:
            count_banned_list[banned] = 0
        count_banned_list[banned] += 1  # 쿼리가 나올때마다 체크, 없으면 추가
        if banned not in banned_list:
            banned_list[banned] = set()
        banned_list[banned].update(
            find_banned_list(user_id, banned)
        )  # 쿼리에 해당하는 id list 찾은 후 추가
        
    result = set()
    for banned in count_banned_list.keys():
        # "****", "****" 의 경우 중복되기 때문에 결국 조합으로 가기로 결정했음
        comb = list(combinations(banned_list[banned], count_banned_list[banned]))
        # 최초에 result가 비어있는 경우 체크
        if len(result) == 0:
            result.update(comb)
            pass
        else:
            # 기존의 데이터들에 하나씩 추가하는 과정
            new_result = set()
            for i in comb:
                for item in result:
                    new_result.add(item + i)
            result = new_result

    remove_dup = set()
    # 중복을 제거하는 과정, 여기서 중복되기때문에 길이가 부족한 친구들 걸러냄
    for item in result:
        tmp = frozenset(list(item))
        if len(tmp) == len(banned_id):
            remove_dup.add(tmp)
    return len(remove_dup)
