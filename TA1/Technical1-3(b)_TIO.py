def pattern_b(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i * 2 - 1:
            print(i, end='')
            j += 1
        print()
        i += 2 


pattern_b(7)