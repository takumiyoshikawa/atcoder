def main():
    n = int(input())
    
    robot = []
    for i in range(n):
        x, l = map(int, input().split())
        robot.append([x-l, x+l])
    
    rs = sorted(robot, key=lambda x: x[1])

    ans = 0
    latest = - 10 ** 10
    for i in range(n):
        if rs[i][0] >= latest:
            latest = rs[i][1]
            ans += 1 

    print(ans)
if __name__=='__main__':
    main()