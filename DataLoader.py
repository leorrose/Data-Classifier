import csv


class Loader:
    """
    class to load data form csv file, create test and training sets of data for Data mining process
    """
    def __init__(self, pathOfFile):
        """"
        Ctor for DataLoader
        Attributes:
            pathOfFile(string): the path to the data set csv file
        """
        self.dataSetPath = pathOfFile
        self.testSet = []
        self.trainingSet = []
        self.structure = []

    def loadData(self):
        """
        method to read data csv file and build data structure, training data set and test data set. data is saved in class parameters
        """
        with open(self.dataSetPath) as csv_file:
            lines, csv_reader = [], csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                lines += [row]
        self.buildStructure(lines)
        self.buildTrainingSet(lines[1:])
        self.buildTestSet(lines[1:])

    def buildStructure(self, lines):
        """"
        method to build structure ( column and their values) of data set
        Returns:
            structure(dict): the structure of data set returns {} if data set is empty, each element is
            columnName : {'index': index , 'values': [values]} or
            columnName : {'index': index , 'values': ["Numeric"]}
        """
        self.structure = self.getColumnsName(lines)
        for column in self.structure.keys():
            self.structure[column]['values'] = self.getColumnValues(list(self.structure.keys()).index(column), lines)

    def getColumnsName(self, lines):
        """"
        method to get columns names from data set
        Attributes:
            lines (list): the lines in data set
        Returns:
            names (list): the names of columns in data set
        """
        names = {}
        for name in lines[0]:
            names[name] = {'index': lines[0].index(name)}
        return names

    def getColumnValues(self, columnIndex, lines):
        """"
        method to get column values from data set
        Attributes:
            lines (list): the lines in data set
            columnIndex (int) : the index of the column to find his values
        Returns:
            values (list): the values of a column in data set
        """
        values = ["Numeric"]
        if not self.isNumeric(columnIndex, lines):
            values = []
            for line in lines[1:]:
                if line[columnIndex] != "" and values.count(line[columnIndex]) == 0:
                    values.append(line[columnIndex])
        return values

    def isNumeric(self, columnIndex, lines):
        """"
        method to check if column is Numeric type of data
        Attributes:
            lines (list): the lines in data set
            columnIndex (int) : the index of the column to find his values
        Returns:
            (boolean) : True if numeric else False
        """
        for line in lines[1:]:
            if line[columnIndex] != "":
                try:
                    int(line[columnIndex])
                except ValueError:
                    try:
                        float(line[columnIndex])
                    except ValueError:
                        return False
        return True

    def buildTrainingSet(self, lines):
        """
        method to create training data set from data
        Attributes:
            lines(list): the lines in data set without first line of column names
        """
        self.trainingSet = lines[0:int(((len(lines)*2)/3) + 0.5)]

    def buildTestSet(self, lines):
        """
        method to create test data set from data
        Attributes:
            lines(list): the lines in data set without first line of column names
        """
        self.testSet = lines[int(((len(lines)*2)/3)+0.5):]


