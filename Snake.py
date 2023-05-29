import random


wall = "************************************************************"
field = ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"]
field2 = ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"]

snake="@"

x=random.randint(1,58)
y=random.randint(0,28)



print(wall)

for i in range(0,y-1):
    for i2 in range(0,59):
        print(field[i2],end="")
    print(field[59])

for i in range(0,len(field)-1):
    if i==x:
        field2[i]="@"

for i in range(0, len(field)-1):
    print(field2[i], end="")
print(field2[len(field2)-1])

for i in range(0,28-y):
    for i2 in range(0, len(field)-1):
        print(field[i2], end="")
    print(field[len(field)-1])

print(wall)

life=True

while life==True:


    where=input("Melyik irányba?")

    if where=="fel" or where=="felfelé":
        print(wall)
        for i in range(0, y - 2):
            for i2 in range(0, 59):
                print(field[i2], end="")
            print(field[59])

        for i in range(0, len(field) - 1):
            print(field2[i], end="")
        print(field2[len(field2) - 1])

        for i in range(0, 29 - y):
            for i2 in range(0, len(field) - 1):
                print(field[i2], end="")
            print(field[len(field) - 1])
        print(wall)
        y-=1

    elif where=="le" or where=="lefelé":
        print(wall)
        for i in range(0, y):
            for i2 in range(0, 59):
                print(field[i2], end="")
            print(field[59])

        for i in range(0, len(field) - 1):
            print(field2[i], end="")
        print(field2[len(field2) - 1])

        for i in range(0, 27 - y):
            for i2 in range(0, len(field) - 1):
                print(field[i2], end="")
            print(field[len(field) - 1])
        print(wall)
        y+=1

    elif where=="jobb" or where=="jobbra":
        print(wall)
        for i in range(0, y - 1):
            for i2 in range(0, 59):
                print(field[i2], end="")
            print(field[59])

        for i in range(0, len(field)):
            if i == x:
                field2[i] = " "
            if i==x+1:
                field2[i] = "@"

        for i in range(0, len(field) - 1):
            print(field2[i], end="")
        print(field2[len(field2) - 1])

        for i in range(0, 28 - y):
            for i2 in range(0, len(field) - 1):
                print(field[i2], end="")
            print(field[len(field) - 1])

        print(wall)
        x+=1
    elif where=="bal" or where=="ballra":
        print(wall)
        for i in range(0, y - 1):
            for i2 in range(0, 59):
                print(field[i2], end="")
            print(field[59])

        for i in range(0, len(field)):
            if i == x:
                field2[i] = " "
            if i==x-1:
                field2[i] = "@"

        for i in range(0, len(field) - 1):
            print(field2[i], end="")
        print(field2[len(field2) - 1])

        for i in range(0, 28 - y):
            for i2 in range(0, len(field) - 1):
                print(field[i2], end="")
            print(field[len(field) - 1])

        print(wall)
        x-=1



    if y==0 or y==29 or x==59 or x==0:
        life=False

else:
    print("oof")