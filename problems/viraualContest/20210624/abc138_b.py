def main():
    n = int(input())
    a = list(map(int, input().split()))

    prodA = 1
    for i in range(n):
        prodA = prodA * a[i]
    
    denominator = 0
    for i in range(n):
        denominator += prodA // a[i]

    if prodA % denominator == 0:
        ans = prodA // denominator
    else:
        ans = prodA / denominator
    print(ans)
if __name__=='__main__':
    main()