import unittest
from DataLoader import Loader


class TestDataLoader(unittest.TestCase):
    dataLoader = None
    dataWithEvenInstances = []
    dataWithOddInstances = []
    dataWithMissingValues = []

    def setUp(self):
        self.dataLoader = Loader("")
        self.dataWithEvenInstances = [["Age", "Income", "class"], ["13", "1000", "yes"], ["18", "5000", "no"],
                                      ["15", "3000", "no"], ["14", "800", "yes"]]
        self.dataWithOddInstances = [["Age", "Income", "class"], ["13", "1000", "yes"], ["18", "5000", "no"],
                                     ["15", "3000", "no"]]
        self.dataWithMissingValues = [["Age", "Income", "class"], ["13", "", "yes"], ["18", "5000", ""],
                                      ["", "3000", "no"]]

    def test_loadData(self):
        # need to read from file
        pass

    def test_buildStructure_dataWithEvenInstances(self):
        self.dataLoader.buildStructure(self.dataWithEvenInstances)

        self.assertEqual({"Age": {"index": 0, "values": ["Numeric"]}, "Income": {"index": 1, "values": ["Numeric"]},
                          "class": {"index": 2, "values": ["yes", "no"]}}, self.dataLoader.structure)

    def test_buildStructure_dataWithOddInstances(self):
        self.dataLoader.buildStructure(self.dataWithOddInstances)

        self.assertEqual({"Age": {"index": 0, "values": ["Numeric"]}, "Income": {"index": 1, "values": ["Numeric"]},
                          "class": {"index": 2, "values": ["yes", "no"]}}, self.dataLoader.structure)

    def test_buildStructure_dataWithMissingValues(self):
        self.dataLoader.buildStructure(self.dataWithMissingValues)

        self.assertEqual({"Age": {"index": 0, "values": ["Numeric"]}, "Income": {"index": 1, "values": ["Numeric"]},
                          "class": {"index": 2, "values": ["yes", "no"]}}, self.dataLoader.structure)

    def test_getColumnsName_dataWithEvenInstances(self):
        self.assertEqual({"Age": {"index": 0}, "Income": {"index": 1}, "class": {"index": 2}},
                         self.dataLoader.getColumnsName(self.dataWithEvenInstances))

    def test_getColumnsName_dataWithOddInstances(self):
        self.assertEqual({"Age": {"index": 0}, "Income": {"index": 1}, "class": {"index": 2}},
                         self.dataLoader.getColumnsName(self.dataWithOddInstances))

    def test_getColumnsName_dataWithMissingValues(self):
        self.assertEqual({"Age": {"index": 0}, "Income": {"index": 1}, "class": {"index": 2}},
                         self.dataLoader.getColumnsName(self.dataWithMissingValues))

    def test_getColumnValues_dataWithEvenInstances(self):
        self.assertEqual(["Numeric"], self.dataLoader.getColumnValues(0, self.dataWithEvenInstances))
        self.assertEqual(["Numeric"], self.dataLoader.getColumnValues(1, self.dataWithEvenInstances))
        self.assertEqual(["yes", "no"], self.dataLoader.getColumnValues(2, self.dataWithEvenInstances))

    def test_getColumnValues_dataWithOddInstances(self):
        self.assertEqual(["Numeric"], self.dataLoader.getColumnValues(0, self.dataWithOddInstances))
        self.assertEqual(["Numeric"], self.dataLoader.getColumnValues(1, self.dataWithOddInstances))
        self.assertEqual(["yes", "no"], self.dataLoader.getColumnValues(2, self.dataWithOddInstances))

    def test_getColumnValues_dataWithMissingValues(self):
        self.assertEqual(["Numeric"], self.dataLoader.getColumnValues(0, self.dataWithMissingValues))
        self.assertEqual(["Numeric"], self.dataLoader.getColumnValues(1, self.dataWithMissingValues))
        self.assertEqual(["yes", "no"], self.dataLoader.getColumnValues(2, self.dataWithMissingValues))

    def test_isNumeric_dataWithEvenInstances(self):
        self.assertEqual(True, self.dataLoader.isNumeric(0, self.dataWithEvenInstances))
        self.assertEqual(True, self.dataLoader.isNumeric(1, self.dataWithEvenInstances))
        self.assertEqual(False, self.dataLoader.isNumeric(2, self.dataWithEvenInstances))

    def test_isNumeric_dataWithOddInstances(self):
        self.assertEqual(True, self.dataLoader.isNumeric(0, self.dataWithOddInstances))
        self.assertEqual(True, self.dataLoader.isNumeric(1, self.dataWithOddInstances))
        self.assertEqual(False, self.dataLoader.isNumeric(2, self.dataWithOddInstances))

    def test_isNumeric_dataWithMissingValues(self):
        self.assertEqual(True, self.dataLoader.isNumeric(0, self.dataWithMissingValues))
        self.assertEqual(True, self.dataLoader.isNumeric(1, self.dataWithMissingValues))
        self.assertEqual(False, self.dataLoader.isNumeric(2, self.dataWithMissingValues))

    def test_buildTrainingSet_dataWithEvenInstances(self):
        self.dataLoader.buildTrainingSet(self.dataWithEvenInstances[1:])

        self.assertEqual([["13", "1000", "yes"], ["18", "5000", "no"], ["15", "3000", "no"]],
                         self.dataLoader.trainingSet)

    def test_buildTrainingSet_dataWithOddInstances(self):
        self.dataLoader.buildTrainingSet(self.dataWithOddInstances[1:])

        self.assertEqual([["13", "1000", "yes"], ["18", "5000", "no"]],
                         self.dataLoader.trainingSet)

    def test_buildTrainingSet_dataWithMissingValues(self):
        self.dataLoader.buildTrainingSet(self.dataWithMissingValues[1:])

        self.assertEqual([["13", "", "yes"], ["18", "5000", ""]],
                         self.dataLoader.trainingSet)

    def test_buildTestSet_dataWithEvenInstances(self):
        self.dataLoader.buildTestSet(self.dataWithEvenInstances[1:])

        self.assertEqual([["14", "800", "yes"]], self.dataLoader.testSet)

    def test_buildTestSet_dataWithOddInstances(self):
        self.dataLoader.buildTestSet(self.dataWithOddInstances[1:])

        self.assertEqual([["15", "3000", "no"]], self.dataLoader.testSet)

    def test_buildTestSet_dataWithMissingValues(self):
        self.dataLoader.buildTestSet(self.dataWithMissingValues[1:])

        self.assertEqual([["", "3000", "no"]], self.dataLoader.testSet)


if __name__ == '__main__':
    unittest.main()