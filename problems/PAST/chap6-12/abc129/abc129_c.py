def main():
    n, m = map(int, input().split())
    MOD = 10 ** 9 + 7
    a = []
    
    cnt = [-1 for _ in range(n+1)]
    cnt[0] = 1
    cnt[1] = 1

    for i in range(m):
        a_i = int(input())
        cnt[a_i] = 0
    
    for i in range(2, n+1):
        if not (cnt[i] == 0):
            cnt[i] = (cnt[i-1] + cnt[i-2]) % MOD

    print(cnt[n])
if __name__=='__main__':
    main()