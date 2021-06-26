def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    aAbs =[]
    neg = 0
    for i in range(n):
        aAbs.append(abs(a[i]))
        if a[i] < 0:
            neg += 1
    
    aAbs_sorted = sorted(aAbs)

    if neg % 2 == 0:
        ans = sum(aAbs)
    else:
        ans = sum(aAbs) - 2 * aAbs_sorted[0]

    print(ans)
if __name__=='__main__':
    main()