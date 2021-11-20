n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

print(' '.join(list(map(str, arr[n::-1]))))
    