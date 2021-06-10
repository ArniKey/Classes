import random


def populate_list(num_elems, max_elem):
  if num_elems >= 0:
    num_elems = int(num_elems)
    #num_elems = float(num_elems)
    l = []
    for i in range(num_elems):
      l.append(random.randint(0, max_elem))
    return l
  else:
    print("ei que aixo es molt petit")

l = []
for i in range(10):
    l.append(i)
print(l)

'''
contador_mes_que_cinc = 0
for i in l:
    if i > 5:
        contador_mes_que_cinc = contador_mes_que_cinc + 1
print(contador_mes_que_cinc)
'''

print(l[0])

# l.reverse()

l_reversed = []
while len(l) > 0:
  element = l[len(l) - 1]
  l.remove(len(l) - 1)
  l_reversed.append(element)

print(len(l))
print(l_reversed)




print(l)
l.sort(reverse=True)
print(l)
l.sort()
print(l)

llista_randoms = populate_list(1, 10)
print(llista_randoms)
llista_randoms = populate_list(1000.0, 10)
print(llista_randoms)

print("l'element numero 6 de la llista random es: " + "cosa" + str(llista_randoms[5]))


