vides = 10
print("Fica aqui la paraula secreta")
paraula_secreta = input()
print("\033[A                                                                                                 \033[A")
paraula_secreta = paraula_secreta.upper()
paraula_joc = []
for i in paraula_secreta:
    paraula_joc += "_"
print(paraula_joc)
while vides > 0 and "_" in paraula_joc:
    print("tens " + str(vides) + " vides")
    lletra = input()
    # Assegurar un sol caracter
    lletra = lletra.upper()
    if lletra in paraula_secreta:
        for i in range(len(paraula_secreta)):
            if lletra == paraula_secreta[i]:
                paraula_joc[i] = lletra
                print(paraula_joc)
    else:
        vides = vides - 1
if vides < 1:
    print("Has perdut" + " la paraula era " + paraula_secreta)





print(paraula_joc)
