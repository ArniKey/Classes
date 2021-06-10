segons = int(input())
resultat = []
dies = segons / 86400
segonssobren = segons % 86400
int(dies)
hores = segons / 3600
int(hores)
minuts = segons / 60
int(minuts)
resultat.append(dies)
resultat.append(hores)
resultat.append(minuts)
print(resultat)
resultat[0] = 0
resultat[1] = 0
resultat[2] = 0
while dies > 0.9:
    dies = dies - 1
    resultat[0] = resultat[0] + 1
else:
    pass
while hores > 0.9:
    hores = hores - 1
    resultat[1] = resultat[1] + 1
else:
    pass
while minuts > 0.9:
    minuts = minuts - 1
    resultat[2] = resultat[2] + 1
else:
    pass

print(resultat)
