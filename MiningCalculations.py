from math import log2


class MiningCalculator:
    def __init__(self):
        pass

    def calcClassEntropy(self, data, structure):
        classIndex, entropy = structure['class']['index'], 0
        for value in structure['class']['values']:
            newData = list(filter(lambda y: y[classIndex] == value, data))
            p = len(newData) / len(data)
            entropy += (-1) * (p * log2(p)) if p > 0 else 0
        return round(entropy, 3)

    def calcClassEntropyByColumn(self, data, structure, colName):
        colIndex, entropy = structure[colName]['index'], 0
        for colValue in structure[colName]['values']:
            newData = list(filter(lambda y: y[colIndex] == colValue, data))
            entropyOfNewData = self.calcClassEntropy(newData, structure)
            entropy += (len(newData)/len(data)) * entropyOfNewData
        return round(entropy, 3)

    def calcClassEntropyBySplit(self, data, structure, colName, splitVal):
        colIndex, entropy = structure[colName]['index'], 0
        newDataBellowSplit = list(filter(lambda y: float(y[colIndex]) <= splitVal, data))
        newDataAboveSplit = list(filter(lambda y: float(y[colIndex]) > splitVal, data))
        entropyOfNewDataBellowSplit = self.calcClassEntropy(newDataBellowSplit, structure)
        entropyOfNewAboveSplit = self.calcClassEntropy(newDataAboveSplit, structure)
        entropy += (len(newDataBellowSplit) / len(data)) * entropyOfNewDataBellowSplit
        entropy += (len(newDataAboveSplit) / len(data)) * entropyOfNewAboveSplit
        return round(entropy, 3)

    def calcInfoGainByColumn(self, data, structure, colName):
        result = self.calcClassEntropy(data, structure) - self.calcClassEntropyByColumn(data, structure, colName)
        result = 0 if result < 0 else result
        return round(result, 3)

    def calcInfoGainBySplit(self, data, structure, colName, splitVal):
        result = self.calcClassEntropy(data, structure) - self.calcClassEntropyBySplit(data, structure, colName, splitVal)
        result = 0 if result < 0 else result
        return round(result, 3)

    def findBestSplitInDataByInfoGain(self, data, structure, colName):
        colIndex, maxInfoGain, bestSplit = structure[colName]['index'], 0, []
        for i in range(0, len(data)-1):
            split = (float(data[i][colIndex]) + float(data[i+1][colIndex])) / 2
            infoGain = self.calcInfoGainBySplit(data, structure, colName, split)
            if infoGain >= maxInfoGain:
                bestSplit = [split, infoGain]
                maxInfoGain = infoGain
        return bestSplit

    def fillBestSplitsInDataByInfoGainIntoSplitList(self, data, structure, colName, numOfSplits, splitsList, indexToInsert):
        if len(data) <= 0 or numOfSplits <= 0:
            return []
        colIndex = structure[colName]['index']
        split = self.findBestSplitInDataByInfoGain(data, structure, colName)
        if str(indexToInsert) in splitsList:
            splitsList[str(indexToInsert)] += [split]
        else:
            splitsList[str(indexToInsert)] = [split]
        indexToInsert, numOfSplits = indexToInsert + 1, numOfSplits - 1

        if split:
            newDataBellowSplit = list(filter(lambda y: float(y[colIndex]) <= split[0], data))
            newDataAboveSplit = list(filter(lambda y: float(y[colIndex]) > split[0], data))
            self.fillBestSplitsInDataByInfoGainIntoSplitList(newDataBellowSplit, structure, colName, numOfSplits, splitsList, indexToInsert)
            self.fillBestSplitsInDataByInfoGainIntoSplitList(newDataAboveSplit, structure, colName, numOfSplits, splitsList, indexToInsert)

    def getBestSplitsInDataByInfoGainInto(self, data, structure, colName, numOfSplits):
        splitsList, newSplitsList = {}, []
        self.fillBestSplitsInDataByInfoGainIntoSplitList(data, structure, colName, numOfSplits, splitsList, 0)
        for lists in list(splitsList.values())[1:]:
            while len(lists) > 0:
                splitOne = lists.pop()
                splitTwo = lists.pop()
                if splitOne and splitTwo:
                    if splitOne[1] >= splitTwo[1]:
                        newSplitsList.append(splitOne[0])
                        newSplitsList.append(splitTwo[0])
                    else:
                        newSplitsList.append(splitTwo[0])
                        newSplitsList.append(splitOne[0])
                elif splitOne:
                    newSplitsList.append(splitOne[0])
                elif splitTwo:
                    newSplitsList.append(splitTwo[0])

        newSplitsList.insert(0, splitsList['0'][0][0])
        return newSplitsList[0:numOfSplits]

