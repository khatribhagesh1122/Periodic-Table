
def mainfunc():
    print("\n\n\n\n********** PERODIC TABLE **********")
    x = int(input("What you want to find :\n\t1 - Atomic no \n\t2 - Atomic Mass\n\t3 - Element\nYour Answer : "))
    if(x==1):
        atno = int(input("Enter Atomic no : "))
        if (atno == 1):
            print("Atomic No : 1\nAtomic Mass No :  1.008\nElement : Hydrogen (H)")
        elif (atno == 2):
            print("Atomic No : 2\nAtomic Mass No :  4.0026\nElement : Helium (He)")
        elif (atno == 3):
            print("Atomic No : 3\nAtomic Mass No :  6.94\nElement : Lithium (Le)")

        again = int(input("Want to find again \n\t If yes press 1 otherwise press enter."))
        if(again == 1):
            mainfunc()

    elif(x==2):
        atmssno = float(input("Enter Atomic Mass no : "))
        if (atmssno == 1.008):
            print("Atomic No : 1\nAtomic Mass No :  1.008\nElement : Hydrogen (H)")
        elif (atmssno == 4.0026):
            print("Atomic No : 2\nAtomic Mass No :  4.0026\nElement : Helium (He)")
        elif (atmssno == 6.94):
            print("Atomic No : 3\nAtomic Mass No :  6.94\nElement : Lithium (Le)")

        again = int(input("Want to find again \n\t If yes press 1 otherwise press enter."))
        if (again == 1):
            mainfunc()
    elif(x==3):
        ele = input("Enter Element : ")
        if (ele == 'Hydrogen' or ele =='H' or ele=='hydrogen' or ele=='h'):
            print("Atomic No : 1\nAtomic Mass No :  1.008\nElement : Hydrogen (H)")
        elif (ele == 'Helium' or ele == 'He' or ele=='helium' or ele=='he'):
            print("Atomic No : 2\nAtomic Mass No :  4.0026\nElement : Helium (He)")
        elif (ele == 'Lithium' or ele == 'Le' or ele == 'lithium' or ele == 'le'):
            print("Atomic No : 3\nAtomic Mass No :  6.94\nElement : Lithium (Le)")

        again = int(input("Want to find again \n If yes press 1 otherwise press enter."))
        if (again == 1):
            mainfunc()
    else:
        print("Enter Valid input...")
        again = int(input("Want to find again \n If yes press 1 otherwise press enter."))
        if (again == 1):
            mainfunc()
mainfunc()
