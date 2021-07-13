def comprovar_triangles(costat1, costat2, costat3):
    if costat1 == costat2 and costat2 == costat3:
        return "equilater"
    if costat1 == costat2 or costat2 == costat3 or costat1 == costat3:
        return "isoceles"
    else:
        return "escalen"


print(comprovar_triangles(2, 20, 0))

