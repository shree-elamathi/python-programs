'''
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters.
You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i]
represents the cost of changing the character original[i] to the character changed[i].
You start with the string source. In one operation, you can pick a character x from the string and change it to the
character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is
impossible to convert source to target, return -1.
Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
'''


def min_cost_to_convert(source, target, original, changed, cost):
    import sys

    # Step 1: Initialize the cost matrix with infinity
    n = 26
    inf = sys.maxsize
    cost_matrix = [[inf] * n for _ in range(n)]

    # Step 2: Fill the initial costs from original to changed characters
    for i in range(len(original)):
        x = ord(original[i]) - ord('a')
        y = ord(changed[i]) - ord('a')
        cost_matrix[x][y] = min(cost_matrix[x][y], cost[i])

    # Step 3: Set the diagonal to zero (cost to convert a character to itself)
    for i in range(n):
        cost_matrix[i][i] = 0

    # Step 4: Floyd-Warshall algorithm to find the minimum cost between all pairs of characters
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cost_matrix[i][j] > cost_matrix[i][k] + cost_matrix[k][j]:
                    cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]

    # Step 5: Calculate the total cost to convert source to target
    total_cost = 0
    for i in range(len(source)):
        s_char = ord(source[i]) - ord('a')
        t_char = ord(target[i]) - ord('a')

        if cost_matrix[s_char][t_char] == inf:
            return -1  # Impossible to convert s_char to t_char

        total_cost += cost_matrix[s_char][t_char]

    return total_cost


# Test cases
source = "abc"
target = "def"
original = ["a", "b", "c", "a"]
changed = ["d", "e", "f", "b"]
cost = [1, 2, 3, 4]

print(min_cost_to_convert(source, target,
