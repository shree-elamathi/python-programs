MOD = 998244353
def calculate_power(N, M, S):
    total_power = 0
    for mask in range(1 << M):
        combined_string = ''
        count = 0
        for i in range(M):
            if mask & (1 << i):
                combined_string += S[i]
                count += S[i].count('a') + S[i].count('b')
        power = pow(2, count, MOD)
        total_power = (total_power + power) % MOD
    return total_power

MOD = 998244353

def calculate_power(current_str, index, strings):
    global total_power
    if index == N:
        power = sum(current_str.count(s) for s in strings)
        total_power = (total_power + pow(2, power, MOD)) % MOD
    else:
        for ch in "abcdefghijklmnopqrstuvwxyz":
            calculate_power(current_str + ch, index + 1, strings)

N, M = map(int, input().split())
strings = [input().strip() for _ in range(M)]
total_power = 0
calculate_power("", 0, strings)
print(total_power)
