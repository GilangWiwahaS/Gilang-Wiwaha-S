from index import ktv


def main():

    p=ktv()

    while (1):
        print("1.Create Customer Detail")
        
        print("2.Rent a Room")

        print("3.Order Food")

        print("4.Songs")

        print("5.Game Station")

        print("6.Total Bill")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            p.inputdata()

        if (b==2):

            p.roomrent()

        if (b==3):

            p.food()

        if (b==4):

            p.Songs()

        if (b==5):

            p.game()

        if (b==6):

            p.display()

        if (b==7):

            quit()



main()
