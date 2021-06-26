def main():
    s = list(input())

    if s[1] == "W":
        if s[6] == "B":
            print("Mi")
        else:
            print("Si")
    else:
        if s[3] == "W":
            if s[8] == "B":
                print("Re")
            else:
                print("La")
        else:
            if s[5] == "B":
                print("Fa")
            else:
                if s[10] == "B":
                    print("Do")
                else:
                    print("So")
if __name__=='__main__':
    main()