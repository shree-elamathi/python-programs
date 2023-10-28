def no_of_people_noticeable(n, ho, a, c, q):
    heights = [ho]
    noticeable_no= 1
    stack = [(ho, 1)]
    for i in range(1, n):
        height = (stack[-1][0] * a + c) % q
        while stack and stack[-1][0] <= height:
            stack.pop()
        if not stack:
            noticeable_no = i + 1
        else:
            noticeable_no += 1
        stack.append((height, i + 1))
    return noticeable_no

n, ho, a, c, q = map(int, input().split())
result = no_of_people_noticeable(n, ho, a, c, q)
print(result)

