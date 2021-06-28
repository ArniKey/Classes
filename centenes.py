def diferents_unitats(numero):
    llista_nums = [1, 2, 3, 4]
    llista_nums[3] = numero % 10
    llista_nums[2] = int((numero - llista_nums[3]) / 10) % 10
    llista_nums[1] = int((numero - (llista_nums[2] * 10) - llista_nums[3]) / 100) % 10
    llista_nums[0] = int((numero - (llista_nums[1] * 100) - (llista_nums[2] * 10) - llista_nums[3]) / 1000) % 10
    print(llista_nums)
    cosaderetornar="kjsdhfksjdfhskjdfhskjdf"



def capturar_xifres(numero):
    llista_nums = []
    while numero != 0:
        llista_nums.append(numero % 10)
        numero = int(numero / 10)
    llista_nums.reverse()
    return llista_nums


nums = capturar_xifres(133432432)
print(nums)