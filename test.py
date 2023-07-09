
def takeInput(var):
    """
    :param var: string name of the Variable
    :return: list of 10 values
    """
    print(f"Ingrese valores de {var}:")
    temp = []
    for i in range(10):
        temp.append(int(input()))
    return temp

A = takeInput("A")
B = takeInput("B")
A.sort()
B.sort()
C = set(A).union(B)

print(f"A ordenado: {' '.join([str(x) for x in A])}")
print(f"B ordenado: {' '.join([str(x) for x in B])}")
print(f"C: {' '.join([str(x) for x in C])}")