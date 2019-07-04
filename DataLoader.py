import csv


class DataLoader:
    def __init__(self, pathOfFile):
        """"
        Ctor for DataLoader
        Attributes:
            pathOfFile(string): the path to the data set csv file
        """
        self.dataSetPath = pathOfFile

    def buildStructure(self):
        """"
        method to build structure ( column and their values) of data set
        Returns:
            structure(list): the structure of data set returns [] if data set is empty, each element is
            [columnName,[values]] or [columnName,"Numeric"]
        """
        with open(self.dataSetPath) as csv_file:
            lines, csv_reader = [], csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                lines += [row]
        structure = self.getColumnsName(lines)
        for columnIndex in range(0, len(structure)):
            structure[columnIndex] += [self.getColumnValues(columnIndex, lines)]
        return structure

    def getColumnsName(self, lines):
        """"
        method to get columns names from data set
        Attributes:
            lines (list): the lines in data set
        Returns:
            names (list): the names of columns in data set
        """
        names = []
        for name in lines[0]:
            names += [[name]]
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
        values = "Numeric"
        if not self.isNumeric(columnIndex, lines[1:]):
            values = []
            for line in lines[1:]:
                if values.count(line[columnIndex]) == 0:
                    values.append(line[columnIndex])
        return values

    def isNumeric(self, columnIndex, lines):
        """"
        method to check if column is Numeric type of data
        Attributes:
            lines (list): the lines in data set
            columnIndex (int) : the index of the column to find his values
        Returns:
            (bollean) : True if numeric else False
        """
        for line in lines:
            try:
                int(line[columnIndex])
            except ValueError:
                try:
                    float(line[columnIndex])
                except ValueError:
                    return False
        return True


path = 'C:/Users/Leor Ariel Rose/Desktop/Dataset.csv'
D = DataLoader(path)
structure = D.buildStructure()
print(structure)