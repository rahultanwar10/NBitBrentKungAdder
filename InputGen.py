import random
numberOfTestCases = 64
numberOfBits = 32
maxNumber = 2**32
inputVectorA = []
inputVectorAint = []
inputVectorB = []
inputVectorBint = []
inputVectorT = []
inputVectorSum = []
inputVectorSumint = []
inputVectorTmain = []
carryOut = []
carryIn = []
carryInint = []
for i in range(0,numberOfTestCases,1):
    inputVectorAint.append(random.randint(0,maxNumber))
for i in inputVectorAint:
    inputVectorA.append(format(i,"b"))
for i in range(0,numberOfTestCases,1):
    carryInint.append(random.randint(0,1))
for i in carryInint:
    carryIn.append(format(i,"b"))
for i in range(len(inputVectorA)):
    if len(inputVectorA[i])<numberOfBits:
        for j in range(numberOfBits - len(inputVectorA[i])):
            inputVectorA[i] = '0' + inputVectorA[i]
for i in range(0,numberOfTestCases,1):
    inputVectorBint.append(random.randint(0,maxNumber))
for i in inputVectorBint:
    inputVectorB.append(format(i,"b"))
for i in range(len(inputVectorB)):
    if len(inputVectorB[i])<numberOfBits:
        for j in range(numberOfBits - len(inputVectorB[i])):
            inputVectorB[i] = '0' + inputVectorB[i]
for i,j,k in zip(inputVectorA,inputVectorB,carryIn):
    inputVectorT.append(i + " " + j + " " + k)
for i,j,k in zip(inputVectorAint,inputVectorBint,carryInint):
    inputVectorSumint.append(i+j+k)
for i in inputVectorSumint:
    inputVectorSum.append(format(i,"b"))
for i in range(len(inputVectorSum)):
    if len(inputVectorSum[i]) > numberOfBits:
        carryOut.append('1')
        inputVectorSum[i] = inputVectorSum[i][1:]
    else:
        carryOut.append('0')
for i in range(len(inputVectorSum)):
    if len(inputVectorSum[i])<numberOfBits:
        for j in range(numberOfBits - len(inputVectorSum[i])):
            inputVectorSum[i] = '0' + inputVectorSum[i]
for i,j,k in zip(inputVectorT,inputVectorSum,carryOut):
    inputVectorTmain.append(i + " " + j + " " + k)
file1 = open("inputVector.txt","w")
for i in inputVectorTmain:
    file1.write(i)
    file1.write('\n')
file1.close()