def main():
    a = [5, 4, 3,2 ,1]
    
    for i in range(len(a)):
        for j in range(len(a) - i -1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

    print(a)

main()