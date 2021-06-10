preu = int(float(input("Fica aquí el preu: ")) * 100)
import_pagat = int(float(input("Fica aquí el que has pagat: ")) * 100)
if preu > import_pagat:
    print("Rata! Paga!")
    exit(1)
canvi_centims = import_pagat - preu
canvi = canvi_centims / 100
print(canvi)


monedes = [200, 100, 50, 20, 10, 5]
quant_monedes = [0, 0, 0, 0, 0, 0]
i = 0
while canvi_centims > 0:
    while canvi_centims >= monedes[i]:
        canvi_centims = canvi_centims - monedes[i]
        quant_monedes[i] = quant_monedes[i] + 1
    i += 1
    if i == 6:
        break



print(quant_monedes)



