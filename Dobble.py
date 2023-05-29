import random
nums=int(input("Kérek egy számot:"))


lista=[]
szam=nums*10

card1=[]
card2=[]
card3=[]
card3=[]


while len(card1)!=nums:
    for i in range(0,nums):
        rand = random.randint(1, 100000)
        if rand not in card1:
            card1.append(rand)
            lista.append(rand)



card2.append(card1[random.randint(0,nums-1)])

while len(card2)!=nums:
    for i in range(0,nums-1):
        rand2 = random.randint(1,100000)
        if rand2 not in lista and rand2 not in card2:
            card2.append(rand2)
            lista.append(rand2)



card31=card1[random.randint(0,nums-1)]
card32=card2[random.randint(0,nums-1)]

if card32==card31:
    card3.append(card32)

else:
    card3.append(card31)
    card3.append(card32)


while len(card3)!=nums:
    if card32!=card31:
        for i in range(0,nums-2):
            rand3 = random.randint(1,100000)
            if rand3 not in lista and rand3 not in card3:
                card3.append(rand3)
                lista.append(rand3)
    else:
        for i in range(0,nums-1):
            rand3 = random.randint(1,100000)
            if rand3 not in lista and rand3 not in card3:
                card3.append(rand3)
                lista.append(rand3)







for i in range(0,nums-1):
    print(card1[i],end=" ")
print(card1[len(card1)-1])

for i in range(0,nums-1):
    print(card2[i],end=" ")
print(card2[len(card2)-1])

for i in range(0,nums-1):
    print(card3[i],end=" ")
print(card3[len(card3)-1])