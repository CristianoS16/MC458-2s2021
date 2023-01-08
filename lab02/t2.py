# Cristiano Sampaio RA: 256352
# Função para encontrar a cadeia consecutiva de maior soma em um vetor
def SCM(vet, nmax):
    n = 1
    while n <= nmax:
        if n == 1:
            if vet[0] < 0:
                i = 0
                j = 0
                k = 0
                maxSeq = 0
                maxSuf = 0
            else:
                i = 1
                j = 1
                k = 1
                maxSeq = vet[0]
                maxSuf = vet[0]
            n += 1
        else:
            if k == 0:
                k = n-1
            maxSuf += vet[n-2]
            if maxSuf > maxSeq:
                i = k
                j = n-1
                maxSeq = maxSuf
            elif (maxSuf == maxSeq and i == k):
                i = k
                j = n-1
                maxSeq = maxSuf
            elif maxSuf < 0:
                maxSuf = 0
                k = 0
            n += 1
    return i, j, k, maxSeq, maxSuf

# Realiza a leitura da entrada
n = int(input())
vet = [int(n) for n in input().split()]

# Retonar resultados
print(SCM(vet, n)[0], SCM(vet, n)[1])