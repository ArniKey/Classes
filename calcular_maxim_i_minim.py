import os
import sys

def calcular_maxim(llista):
    maxim = float("-inf")
    for i in llista:
        if i > maxim:
            maxim = i
    return maxim


def calcular_minim(llista):
    minim = float("inf")
    for i in llista:
        if i < minim:
            minim = i
    return minim


print(calcular_minim([10, 2.0, 20, 30, 10.2, 60, 45]))
print(calcular_maxim([10, 20.9, 20, 30, 10, 60.9, 45]))