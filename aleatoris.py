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


def minuscula_dins_rang(lletra1, lletra2):
    numero_random = aleatori_amb_minim(ord(lletra1), ord(lletra2))
    lletra_random = chr(numero_random)
    return(lletra_random)


print(minuscula_dins_rang('d', 'l'))


def decimal_random(minim, maxim):
    minim = int(minim * 100)
    maxim = int(maxim * 100)
    decimal_aleatori = aleatori_amb_minim(minim, maxim)
    decimal_aleatori = float(decimal_aleatori / 100)
    return decimal_aleatori


print(decimal_random(2.11, 2.99))