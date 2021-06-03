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

def es_data_correcta(data_any):
    camps = data_any.split("/")

    for i in range(len(camps)):
        camps[i] = int(camps[i])

    if camps[0] > 31:
        return 0
    if camps[1] > 12:
        return 0
    mesos = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mesos[camps[1] - 1] < camps[0]:
        return 0
    print(camps[0])
    if camps[0] == 29 and camps[1] == 2:
        if es_bixest(camps[2]):
            return 1
        else:
            return 0
    else:
        return 1












print(es_bixest(1001))
print("canvis")
print(es_data_correcta("29/02/1998"))

