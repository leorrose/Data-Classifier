from DataClassifier import Classifier
from DataCleaner import Cleaner
from DataDiscretization import Discretization
from DataLoader import Loader
from MiningCalculations import MiningCalculator
from FileCreator import CreateFile


class BuildClassifierProcess:
    def __init__(self):
        pass

    def setClassifierType(self, classifierType):
        self.classifierType = classifierType
        return self

    def setClassifierSplitType(self, classifierSplitType):
        self.classifierSplitType = classifierSplitType
        return self

    def setDiscretizationType(self, discretizationType):
        self.discretizationType = discretizationType
        return self

    def setDiscretizationBins(self, discretizationBins):
        self.discretizationBins = discretizationBins
        return self

    def setFolderPath(self, folderPath):
        self.folderPath = folderPath
        return self

    def setSavingFolderPath(self, savingFolderPath):
        self.savingFolderPath = savingFolderPath
        return self

    def startProcess(self):
        fileCreator, dataCleaner, dataDiscretization, Calculator, dataClassifier, dataLoader = CreateFile(), Cleaner(), Discretization(),\
                                                                                               MiningCalculator(), Classifier(), Loader()
        splitFunction = Calculator.getSplitFunc(self.classifierSplitType)

        try:
            dataLoader.loadData(self.folderPath)

            dataCleaner.cleanTrainingSet(dataLoader.trainingSet, dataLoader.structure)
            dataCleaner.cleanTestSet(dataLoader.testSet, dataLoader.structure)
            fileCreator.createCsvFile(dataLoader.structure, dataLoader.trainingSet, "Clean Training set", self.savingFolderPath)
            fileCreator.createCsvFile(dataLoader.structure, dataLoader.testSet, "Clean Test set", self.savingFolderPath)

            dataDiscretization.discretizationData(dataLoader.trainingSet, dataLoader.testSet, dataLoader.structure, self.discretizationBins,
                                                  self.discretizationType)
            fileCreator.createCsvFile(dataLoader.structure, dataLoader.trainingSet, "Discretization Training set", self.savingFolderPath)
            fileCreator.createCsvFile(dataLoader.structure, dataLoader.testSet, "Discretization Test set", self.savingFolderPath)

            classifier = dataClassifier.buildClassifier(dataLoader.trainingSet, dataLoader.structure, self.classifierType, splitFunction)
            classifiedTestData = dataClassifier.classifyTest(dataLoader.testSet, dataLoader.structure, classifier, self.classifierType)
            fileCreator.createCsvFile(dataLoader.structure,  classifiedTestData, "Classified Test set", self.savingFolderPath)
            accuracy = dataClassifier.checkAccuracyOfClassifier(classifiedTestData, dataLoader.testSet)
            classifier += ["accuracy: " + str(accuracy)]
            fileCreator.createTxtFile(classifier, "Rules", self.savingFolderPath)

            return " Classifier build successfully with accuracy: " + str(accuracy)

        except EnvironmentError:
            return "Problem with file\\ file path. please check file is not empty and file path is correct!"

        except ValueError:
            return "number of bins must be at least as number of class values!"

class ClassifyProcess:
    def __init__(self):
        pass

    def setRulesPath(self, rulesPath):
        self.rulesPath = rulesPath
        return self

    def setFolderPath(self, folderPath):
        self.folderPath = folderPath
        return self

    def setSavingFolderPath(self, savingFolderPath):
        self.savingFolderPath = savingFolderPath
        return self

    def classifyFile(self):
        pass


