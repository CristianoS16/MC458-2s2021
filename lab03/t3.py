# Cristiano Sampaio RA: 256352

#Intercala + conta flips
def intercala(vet, p, q, r):
    #Contador para os flips
    cont=0
    #Faz uma copia do vetor
    aux = vet[p:r+1]
    #Define algumas variaveis para percorrer o vetor auxiliar e intercalar os elementos
    i=0
    j=q+1-p
    k=p
    #Percorre vetor auxiliar corrigindo vetor original
    while i<=q-p and j<=r-p:
        if aux[i]<aux[j]:
            vet[k]=aux[i]
            i+=1
        else:
            vet[k]=aux[j]
            j+=1
            cont+= q-i+1-p
        k+=1
    #Caso quando todos os elementos de um lado do vetor já foram intercalados, simplesmente copia o outro lado do vetor
    while i<=q-p:
        vet[k]=aux[i]
        i+=1
        k+=1
    
    while j<=r-p:
        vet[k]=aux[j]
        j+=1
        k+=1
        cont+= q-i+1-p
    return cont

#MergeSorte + acumula número de flips a cada chamada
def mergeSort(vet, p, r):
    cont = 0
    if p<r:
        q = (p+r)//2
        cont+=mergeSort(vet, p, q)
        cont+=mergeSort(vet, q+1, r)
        cont+= intercala(vet, p, q, r)
    return cont

#Ler entrada
n = int(input())
vet = [int(n) for n in input().split()]
#Imprime o numero de flips
print(mergeSort(vet, 0, n-1))