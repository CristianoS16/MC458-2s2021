# Cristiano Sampaio Pinheiro
#RA: 256352

# Realiza leitura das entradas que sao arrays
def readArray():
    inList = input()
    inputList = inList.split()
    for i in range(len(inputList)):
        inputList[i] = int(inputList[i])
    return inputList


# Realiza o acesso MTF
def mtfAccess():
    internalList = itemsList.copy()
    cont = 0
    for i in range(totalRequests):
        if(requestes[i] > totalItems or requestes[i] < 1):
            cont = cont+totalItems+1
        else:
            for j in range(totalItems):
                if(requestes[i] == internalList[j]):
                    cont = cont+j+1
                    aux = internalList[j]
                    while(j > 0):
                        internalList[j] = internalList[j-1]
                        j = j-1
                    internalList[0] = aux
    return cont

# Realiza o acesso TRANS
def transAccess():
    internalList = itemsList.copy()
    cont = 0
    for i in range(totalRequests):
        if(requestes[i] > totalItems or requestes[i] < 1):
            cont = cont+totalItems+1
        else:
            for j in range(totalItems):
                if(requestes[i] == internalList[j]):
                    cont = cont+j+1
                    if(j != 0):
                        aux = internalList[j]
                        internalList[j] = internalList[j-1]
                        internalList[j-1] = aux
    return cont

# Realiza o acesso FC
def fcAccess():
    internalList = itemsList.copy()
    frequencyList = [0] * totalItems
    cont = 0
    for i in range(totalRequests):
        if(requestes[i] > totalItems or requestes[i] < 1):
            cont = cont+totalItems+1
        else:
            for j in range(totalItems):
                if(requestes[i] == internalList[j]):
                    cont = cont+j+1
                    frequencyList[j] = frequencyList[j] + 1
                    aux = internalList[j]
                    currentFrequency = frequencyList[j]
                    while(j > 0 and currentFrequency >= frequencyList[j-1]):
                        internalList[j] = internalList[j-1]
                        frequencyList[j] = frequencyList[j-1]
                        j = j-1
                    internalList[j] = aux
                    frequencyList[j] = currentFrequency
    return cont

# Realiza a operacao not no bit, que no e um inteiro
def notBit(bit):
    if(bit == 1):
        return 0
    return 1

# Realiza o acesso BIT
def bitAccess():
    internalList = itemsList.copy()
    cont = 0
    for i in range(totalRequests):
        if(requestes[i] > totalItems or requestes[i] < 1):
            cont = cont+totalItems+1
        else:
            for j in range(totalItems):
                if(requestes[i] == internalList[j]):
                    cont = cont+j+1
                    bitsList[j] = notBit(bitsList[j])
                    if(bitsList[j] == 0):
                        aux = internalList[j]
                        while(j > 0):
                            internalList[j] = internalList[j-1]
                            bitsList[j] = bitsList[j-1]
                            j = j-1
                        internalList[0] = aux
                        bitsList[0] = 0
    return cont

totalItems = int(input())
itemsList = readArray()
bitsList = readArray()
totalRequests = int(input())
requestes = readArray()

print(mtfAccess())
print(transAccess())
print(fcAccess())
print(bitAccess())
