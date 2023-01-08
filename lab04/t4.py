#Cristiano Sampaio Pinheiro RA:256352

def countingSort(A, B, n, k, j):
    C = [0]*k
    for i in range(n):
        C[ord(A[i][j])-48]+=1
    for h in range(1,k):
        C[h]=C[h]+C[h-1]
    for i in range(n-1, -1, -1):
        B[C[ord(A[i][j])-48]-1] = A[i]
        C[ord(A[i][j])-48] = C[ord(A[i][j])-48]-1
    return B

def radixSort(A, B, n, k):
    for j in range(30, -1, -1):
        if(A[0][j]!=' '):
            A = countingSort(A, B, n, k, j).copy()
    return A

#Imprime a saida
def printAccounts(A, n):
    i = 0
    while i<n:
        cont=0
        contAccounts = n
        while i+1<n and A[i]==A[i+1]:
            del(A[i+1])
            cont += 1
            n-=1
        contAccounts -= cont
        A[i] = "".join((A[i]," "+str(cont+1)))
        i += 1
    print(contAccounts)
    for s in A:
        print(s)     


#Ler entrada
A = []
n = int(input())
for i in range(n):
    A.append(input())

k = 23
B = [0]*n
A = radixSort(A, B, n ,k)
printAccounts(A, n)