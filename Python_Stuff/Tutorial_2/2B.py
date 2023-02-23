import math
def main():
    radius = input("Please enter the radius: ")
    while(not radius.replace('.','', 1).isdigit()):
        radius = input("Radius must be a integer or float: ")

    radius = float(radius)

    print()
    print("Results in 3 decimal places ")
    print("Diameter is \t \t {:.3f}".format(radius*2))
    print("Circumference is \t {:.3f}".format(math.pi*2*radius))
    print("Surface Area is \t {:.3f}".format(4*math.pi* radius**2))
    print("Volume is \t \t {:.3f}".format((4/3)*math.pi*radius**3))


main()
