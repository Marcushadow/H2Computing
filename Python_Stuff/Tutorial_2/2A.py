def main():
    name = input("Input your name: ")
    age = input("Input your age: ")
    while(not age.isdigit()):
        age = input("Age must be a number:")
    age = int(age)

    print("Welcome {} , Age : {}, Age in 10 Years : {}".format(name, age, age+10))

main()
