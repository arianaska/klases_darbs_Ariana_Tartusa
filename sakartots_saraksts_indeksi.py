#1. Izveidot sarakstu,izmantojot list
skaitli= [4,8,12,16,20,24,28,32,36]

print(skaitli)
print(skaitli[0]) 
print(skaitli[4])

#2. Izveidot minēšanas spēli,izmantojot bināro mēklēšanu

sakums = 1
beigas = 100
print("Iedomājies skaitli no 1 līdz 100!")
while sakums <= beigas:
    videjais = (sakums + beigas) // 2
    atbilde = input("Vai skaitlis ir "+ str(videjais)+ "? (lielāks/mazāks/jā): ")

    if atbilde == "jā":
        print(f"Es uzminēju!")
        break
    elif atbilde == "lielāks":
        sakums = videjais + 1
    elif atbilde == "mazāks":
        beigas = videjais - 1