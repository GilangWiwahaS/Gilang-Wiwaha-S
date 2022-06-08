class ktv:

    def __init__(self,bill='',song=0,games=0,ruang=0,foods=0,service=10,name='',address=''):

        print ("\n\n*****KARAOKE BILLING SYSTEM*****\n")

        self.bill=bill
        self.song=song
        self.games=games
        self.ruang=ruang
        self.foods=foods
        self.service=service
        self.name=name
        self.address=address

    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")

    def roomrent(self):

        print ("We have the following rooms for you:-")

        print ("1.  Type A---->$50")

        print ("2.  Type B---->$40")

        print ("3.  Type C---->$30")

        print ("4.  Type D---->$20")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("You Have Opted Room Type A")

            self.ruang=50*n

        elif (x==2):

            print ("You Have Opted Room Type B")

            self.ruang=40*n

        elif (x==3):

            print ("You Have Opted Room Type C")

            self.ruang=30*n

        elif (x==4):
            print ("You Have Opted Room Type D")

            self.ruang=20*n

        else:

            print ("Please Choose A Room")

        print ("Your Room Rent Is =",self.ruang,"\n")

    def food(self):

        print("*****FOOD MENU*****")

        print("1.Juice---->$1")
        print("2.Tea------>$2")
        print("3.Meal----->$5")
        print("4.Sneak---->$7")
        print("5.Salad---->$8")
        print("6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.foods=self.foods+1*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.foods=self.foods+2*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.foods=self.foods+5*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.foods=self.foods+7*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.foods=self.foods+8*d

            elif (c==6):
                break
            else:
                print("Invalid option")

        print ("Total food Cost=$",self.foods,"\n")

    def	Songs(self):
        print ("******SONGS MENU*******")

        print ("1.Happy-------->$1")
        print ("2.Tabun-------->$1")
        print ("3.Alone-------->$2")
        print ("4.Lily--------->$2")
        print ("5.Yamiy-------->$2")
        print ("6.Exit")

        while (1):

            e=int(input("Enter Number: "))

            if e==1:
                f=int(input("Enter The Hours:"))
                self.song=self.song+1*f
            elif (e==2):
                    f=int(input("Enter The Hours:"))
                    self.song=self.song+1*f

            elif (e==3):
                    f=int(input("Enter The Hours:"))
                    self.song=self.song+2*f

            elif (e==4):
                    f=int(input("Enter The Hours:"))
                    self.song=self.song+2*f

            elif (e==5):
                    f=int(input("Enter The Hours:"))
                    self.song=self.song+2*f

            elif (e==6):
                break
            else:

                print ("Invalid option")


        print ("Total Laundary Cost=$",self.song,"\n")

    def game(self):
        print ("******GAME MENU*******")

        print ("1.Table Tennis----->$5")
        print ("2.Bowling---------->$5")
        print ("3.Billiard--------->$6")
        print ("4.Video Games------>$2")
        print ("5.Pool------------->$5")
        print ("6.Exit")

        while (1):

            
            g=int(input("Enter your choice:"))


            if g==1:
                h=int(input("No. of hours:"))
                self.games=self.games+5*h

            elif g==2:
                h=int(input("No. of hours:"))
                self.games=self.games+5*h

            elif g==3:
                h=int(input("No. of hours:"))
                self.games=self.games+6*h

            elif g==4:
                h=int(input("No. of hours:"))
                self.games=self.games+2*h

            elif g==5:
                h=int(input("No. of hours:"))
                self.games=self.games+5*h
            elif g==6:
                break

            else:

                print ("Invalid option")

        print ("Total Game Bill=$",self.games,"\n")

    def display(self):
        print ("******Total BILL******")
        print ("------Customer details-------")
        print ("------Customer name:",self.name)
        print ("------Customer address:",self.address)
        print ("------Your Room rent is:",self.ruang)
        print ("------Your Food bill is:",self.foods)
        print ("------Your Song bill is:",self.song)
        print ("------Your Game bill is:",self.games)

        self.bill=self.song+self.foods+self.games+self.ruang

        print ("------Your sub total bill is:",self.bill)
        print ("------Additional Service Charges is",self.service)
        print ("------Your grandtotal bill is:",self.bill+self.service,"\n")
