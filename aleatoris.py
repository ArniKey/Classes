import random


def aleatori():
    numero_random = random.randint(0, 32767)
    return numero_random


print(aleatori())


def aleatori_dins_rang(numero):
    numero = aleatori() % numero
    return numero


print(aleatori_dins_rang(11))


def aleatori_amb_minim(minim, maxim):
    numero_random = aleatori_dins_rang(maxim - minim) + minim
    return numero_random


print(aleatori_amb_minim(15, 20))


def lletra_aleatoria():
    abecedari = []
    for num_lletra in range(65, 65 + 26):
        abecedari.append(chr(num_lletra))
    index = aleatori_dins_rang(26)
    lletra = abecedari[index]
    return lletra





print(lletra_aleatoria())