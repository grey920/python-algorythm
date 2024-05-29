n = int(input())

for i in range( 1, 2 * n ):
    for j in range( 1, 2 * n + 1 ):
        # i == n 이면, 2 * n 개 출력
        if i == n:
            print("*", end="")
        else:
            # i가 n보다 작을 때, j가 i보다 작거나 같으면 별 출력
            if n > i:
                if i >= j or j >= 2 * n - i + 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            # i가 n보다 클 때, j가 2n - i + 1보다 같거나 작으면 별 출력
            else:
                if j < 2*n - i + 1 or i < j:
                    print("*", end="")
                else:
                    print(" ", end="")
    print()