yes = 1
while yes:
    yes = input("Continoue the running program (yes/no) : ")
    if yes.upper() == "NO":
        print("Program exit Bye.....")
        break
    else:
        no = int(input("Enter the number "))
        for i in range(1, 11):
            print(no*i)
