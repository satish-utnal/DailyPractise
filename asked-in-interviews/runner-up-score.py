def p_l(arr):
    arr1 = set(arr)
    arr2 = sorted(arr1)
    arr3 = list(arr2)
    print(arr3[-2])


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    p_l(arr)