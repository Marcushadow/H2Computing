def main():
    hourlyWage = input("Please input your hourly wage: ")
    while(not hourlyWage.replace('.', '', 1).isdigit()):
        hourlyWage = input("Hourly wage must either be an integer or float (No negatives): ")

    regularHours = input("Please input your regular hours: ")
    while(not regularHours.replace('.', '', 1).isdigit()):
        regularHours = input(
            "Regular hours must either be an integer or float (No negatives): ")

    overtimeHours = input("Please input your overtime hours: ")
    while(not overtimeHours.replace('.', '', 1).isdigit()):
        overtimeHours = input("Overtime hours must either be an integer or float (No negatives): ")

    hourlyWage = float(hourlyWage)
    regularHours = float(regularHours)
    overtimeHours = float(overtimeHours)

    totalPay = hourlyWage * regularHours + 1.5 * hourlyWage*overtimeHours

    print("The total pay is ${:.0f}".format(totalPay))


main()
