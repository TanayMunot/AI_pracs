import random
import math


def crossover():
    str1 = input("enter 1st genes")
    str2 = input("enter 2nd genes")
    gene1 = list(str1)
    gene2 = list(str2)
    n = len(gene1)
    k = math.floor(random.random() * n)
    print(f"crossover point is: {k}")
    final_genes1 = list()
    final_genes2 = list()
    index = 0
    while index < n:
        if index < k:
            final_genes1.append(gene1[index])
            final_genes2.append(gene2[index])
        else:
            final_genes1.append(gene2[index])
            final_genes2.append(gene1[index])
        index += 1
    final_str1 = ""
    final_str2 = ""
    for bit in final_genes1:
        final_str1 += bit
    for bit in final_genes2:
        final_str2 += bit
    print("Parent 1 : {}".format(str1))
    print("Parent 2 : {}".format(str2))
    print("Offspring 1 : {}".format(final_str1))
    print("Offspring 2 : {}".format(final_str2))

crossover()