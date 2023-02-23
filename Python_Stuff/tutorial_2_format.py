def main():
    amount = 24.32578923
    print("{:0.3f}".format(amount))
    print("{:1.3f}".format(amount))
    print("{:2.3f}".format(amount))
    print("{:3.3f}".format(amount))
    print("{:4.3f}".format(amount))
    print("{:5.3f}".format(amount))
    print("{:6.3f}".format(amount))
    print("{:-08.3f}".format(amount))

    for i in range (2,1,-1):
        print(i)

main()