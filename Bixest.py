def es_bixest(any_bixest):
    if any_bixest % 4 == 0:
        if any_bixest % 100 == 0:
            if any_bixest % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

any_bixest = int(input())
resultat = es_bixest(any_bixest)
print(resultat)



