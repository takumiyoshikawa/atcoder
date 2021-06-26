def main():
    h,w = map(int, input().split())
    MOD = 10 ** 9 + 7

    a =[]
    for i in range(h):
        a.append(list(input()))
    
    
    cnt = [[0] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                cnt[i][j] = 0
            else:
                if i == 0 and j ==0:
                    cnt[i][j] = 1
                elif i == 0:
                    cnt[i][j] = cnt[i][j-1] % MOD
                elif j == 0:
                    cnt[i][j] = cnt[i-1][j] %MOD
                else:
                    cnt[i][j] = (cnt[i-1][j] + cnt[i][j-1]) % MOD

    print(cnt[h-1][w-1])

if __name__=='__main__':
    main()