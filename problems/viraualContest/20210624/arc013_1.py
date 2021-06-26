def main():
    n, m, l = map(int, input().split())
    p, q, r = map(int, input().split())

    numRec = max((n//p) * (m//q), (m//p) * (n//q))
    numHeight = l // r

    ans = numRec * numHeight
    print(ans)
if __name__=='__main__':
    main()