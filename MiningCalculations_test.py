import unittest
from MiningCalculations import MiningCalculator


class TestDataLoader(unittest.TestCase):
    calculator = None
    dataOne = []
    dataTwo = []
    structureOne = []
    structureTwo = []

    def setUp(self):
        self.calculator = MiningCalculator()
        self.dataOne = [["4", "no"], ["5", "yes"], ["8", "no"], ["12", "yes"], ["15", "yes"]]
        self.structureOne = {"Hours": {"index": 0, "values": ["Numeric"]},
                             "class": {"index": 1, "values": ["no", "yes"]}}
        self.dataTwo = [["M", "Diaspora", "Over 700", "High"], ["M", "Israel", "600-700", "Medium"],
                        ["F", "Israel", "600-700", "High"], ["F", "Diaspora", "0-600", "Medium"],
                        ["F", "Israel", "0-600", "Low"]]
        self.structureTwo = {"Gender": {"index": 0, "values": ["M", "F"]},
                             "Place": {"index": 1, "values": ["Diaspora", "Israel"]},
                             "Test": {"index": 2, "values": ["0-600", "600-700", "Over 700"]},
                             "class": {"index": 3, "values": ["Low", "Medium", "High"]}}

    def test_calcClassEntropy(self):
        self.assertEqual(0.971, self.calculator.calcClassEntropy(self.dataOne, self.structureOne))
        self.assertEqual(1.522, self.calculator.calcClassEntropy(self.dataTwo, self.structureTwo))

    def test_calcClassEntropyByColumn(self):
        self.assertEqual(1.351, self.calculator.calcClassEntropyByColumn(self.dataTwo, self.structureTwo, "Gender"))
        self.assertEqual(1.351, self.calculator.calcClassEntropyByColumn(self.dataTwo, self.structureTwo, "Place"))
        self.assertEqual(0.800, self.calculator.calcClassEntropyByColumn(self.dataTwo, self.structureTwo, "Test"))

    def test_calcClassEntropyBySplit(self):
        self.assertEqual(0.649, self.calculator.calcClassEntropyBySplit(self.dataOne, self.structureOne, "Hours", 4.5))
        self.assertEqual(0.951, self.calculator.calcClassEntropyBySplit(self.dataOne, self.structureOne, "Hours", 6.5))
        self.assertEqual(0.551, self.calculator.calcClassEntropyBySplit(self.dataOne, self.structureOne, "Hours", 10))
        self.assertEqual(0.8, self.calculator.calcClassEntropyBySplit(self.dataOne, self.structureOne, "Hours", 13.5))

    def test_calcInfoGainByColumn(self):
        self.assertEqual(0.171, self.calculator.calcInfoGainByColumn(self.dataTwo, self.structureTwo, "Gender"))
        self.assertEqual(0.171, self.calculator.calcInfoGainByColumn(self.dataTwo, self.structureTwo, "Place"))
        self.assertEqual(0.722, self.calculator.calcInfoGainByColumn(self.dataTwo, self.structureTwo, "Test"))

    def test_calcInfoGainBySplit(self):
        self.assertEqual(0.322, self.calculator.calcInfoGainBySplit(self.dataOne, self.structureOne, "Hours", 4.5))
        self.assertEqual(0.02, self.calculator.calcInfoGainBySplit(self.dataOne, self.structureOne, "Hours", 6.5))
        self.assertEqual(0.42, self.calculator.calcInfoGainBySplit(self.dataOne, self.structureOne, "Hours", 10))
        self.assertEqual(0.171, self.calculator.calcInfoGainBySplit(self.dataOne, self.structureOne, "Hours", 13.5))

    def test_findBestSplitInDataByInfoGain(self):
        self.assertEqual([10, 0.42],
                         self.calculator.findBestSplitInDataByInfoGain(self.dataOne, self.structureOne, "Hours"))

    def test_fillBestSplitsInDataByInfoGainIntoSplitList(self):
        splitList = {}

        self.calculator.fillBestSplitsInDataByInfoGainIntoSplitList(self.dataOne, self.structureOne,
                                                                    "Hours", 2, splitList, 0)
        self.assertEqual({"0": [[10.0, 0.42]], '1': [[6.5, 0.251], [13.5, 0.0]]}, splitList)

    def test_getBestSplitsInDataByInfoGainInto(self):
        self.assertEqual([10, 6.5],
                         self.calculator.getBestSplitsInDataByInfoGainInto(self.dataOne, self.structureOne, "Hours", 2))

        self.assertEqual([10, 6.5, 13.5, 4.5],
                         self.calculator.getBestSplitsInDataByInfoGainInto(self.dataOne, self.structureOne, "Hours", 5))


if __name__ == '__main__':
    unittest.main()