t = int(input())
ks = [int(input()) for _ in range(t)]

for k in ks:
    count = 0
    n = 1
    while True:
        if n % 3 != 0 and n % 10 != 3:
            count += 1
            if count == k:
                print(n)
                break
        n += 1
