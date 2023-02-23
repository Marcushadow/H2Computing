def main():
    a = [5, 4, 3, 2, 1]

    for i in range(len(a)):
        for j in range(i,0, -1):
            if(a[j] < a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break

    print(a)


main()
