#1. Ievadi skaitli no 1 līdz 15 ieskaitot
for i in range(1, 16):
    print(i)
    
#2. No 1 līdz 30 saskaiti skaitļus,kas dalās ar 4,un aprēķini to summu
summa_dalas_ar_4= 0

print("\nSkaitļi,kas dalās ar 4:")
for i in range(1, 31):
    if i % 4 == 0:
        print(i)
        summa_dalas_ar_4 += i

print(f"\nTo skaitļu summa, kas dalās ar 4, ir: {summa_dalas_ar_4}")

#3. Ievadīt 5 skaitļus un aprēķināt to summu, ka arī atsevišķi saskaitīt pozitīvos,negatīvos skaitļus un nulles
summa = 0
pozitīvo_skaits = 0
negatīvo_skaits = 0
nulles_skaits = 0

for i in range(5):
    skaitlis = float(input(f"Ievadiet {i+1}. skaitli: "))
    summa += skaitlis
    if skaitlis > 0:
        pozitīvo_skaits += 1
    elif skaitlis < 0:
        negatīvo_skaits += 1
    else:
        nulles_skaits += 1

print("Ievadīto skaitļu summa:", summa)
print("Pozitīvo skaitļu skaits:", pozitīvo_skaits)
print("Negatīvo skaitļu skaits:", negatīvo_skaits)
print("Nulles skaits:", nulles_skaits)