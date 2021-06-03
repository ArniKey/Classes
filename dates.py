def es_bixest(any_bixest):
    if any_bixest % 4 == 0:
        if any_bixest % 100 == 0:
            if any_bixest % 400 == 0:
                return 1
            else:
                returngi 0
        else:
            return 1
    else:
        return 0

print(es_bixest(1001))
print("canvis")