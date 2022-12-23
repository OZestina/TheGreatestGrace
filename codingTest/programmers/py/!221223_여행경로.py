# https://school.programmers.co.kr/learn/courses/30/lessons/43164?itm_content=course14743#

# 1st try
# 


# 2nd try (다른 사람의 풀이) => 아직 안봄..! 봐야함!!

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]
