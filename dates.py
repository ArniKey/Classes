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


def compare_dates(data1, data2):
    if es_data_correcta(data1) != 1 or es_data_correcta(data2) != 1:
        print("format incorrecte!!")
        exit(1)
    camps1 = data1.split("/")
    camps2 = data2.split("/")

    flag = 0
    for i in range(len(camps1)):
        if camps1[i] != camps2[i]:
            flag = 1
            break
    if flag == 0:
        return 0
    else:
        for i in range(len(camps1)).__reversed__():
            if camps1[i] > camps2[i]:
                return 1
            elif camps1[i] < camps2[i]:
                return -1
            else:
                continue














print(es_bixest(1001))
print("canvis")
print(es_data_correcta("29/02/1998"))
data1 = "28/04/1992"
data2 = "28/07/1992"
print(compare_dates(data1, data2))


