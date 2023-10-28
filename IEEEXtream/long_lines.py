def is_noticeable(heights, i, j):
    for k in range(i + 1, j):
        if heights[k] >= heights[i]:
            return False
    return True
def count_noticeable_people(n, h_0, a, c, q):
    heights = [h_0]
    for i in range(1, n):
        heights.append((a * heights[i - 1] + c) % q)

    noticeable_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_noticeable(heights, i, j):
                noticeable_count += 1
    return noticeable_count
def main():
    n, h_0, a, c, q = map(int, input().split())
    noticeable_count = count_noticeable_people(n, h_0, a, c, q)
    print(noticeable_count)


if __name__ == "__main__":
    main()

