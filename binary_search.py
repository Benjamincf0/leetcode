l = [2, 4, 5, 7, 9, 12, 13, 14, 16]

def binary_search(l: list, n: int):
    left = 0
    right = len(l) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_val = l[mid_idx]

        if n > mid_val:
            left = mid_idx + 1
        elif n < mid_val:
            right = mid_idx - 1
        else:
            return mid_idx
    return -1

if __name__ == "__main__":
    print(binary_search(l, 2))
    print(binary_search(l, 14))
