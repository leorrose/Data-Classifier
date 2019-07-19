import unittest
from DataClassifier import Classifier
from MiningCalculations import MiningCalculator


class TestDataLoader(unittest.TestCase):
    calculator = None
    data = []
    structure = []

    def setUp(self):
        self.classifier = Classifier()
        self.calculator = MiningCalculator()
        self.data = [["M", "Diaspora", "Over 700", "High"], ["M", "Israel", "600-700", "Medium"],
                     ["F", "Israel", "600-700", "High"], ["F", "Diaspora", "0-600", "Medium"],
                     ["F", "Israel", "0-600", "Low"]]
        self.structure = {"Gender": {"index": 0, "values": ["M", "F"]},
                          "Place": {"index": 1, "values": ["Diaspora", "Israel"]},
                          "Test": {"index": 2, "values": ["0-600", "600-700", "Over 700"]},
                          "class": {"index": 3, "values": ["Low", "Medium", "High"]}}

    def test_buildClassifier(self):
        rules = self.classifier.buildClassifier(self.data, self.structure, "id3", self.calculator.findBestColumnSplitByInfoGain)

        self.assertEqual(['Test == 0-600 , Place == Diaspora => class == Medium', 'Test == 0-600 , Place == Israel => class == Low',
                          'Test == 600-700 , Gender == M => class == Medium', 'Test == 600-700 , Gender == F => class == High',
                          'Test == Over 700 => class == High'], rules)

    def test_buildId3Classifier(self):
        rules = self.classifier.buildId3Classifier(self.data, self.structure, "Medium", self.calculator.findBestColumnSplitByInfoGain)

        self.assertEqual(['Test == 0-600 , Place == Diaspora => class == Medium', 'Test == 0-600 , Place == Israel => class == Low',
                          'Test == 600-700 , Gender == M => class == Medium', 'Test == 600-700 , Gender == F => class == High',
                          'Test == Over 700 => class == High'], rules)

    def test_convertStringRulesToLists(self):
        rules = self.classifier.buildId3Classifier(self.data, self.structure, "Medium", self.calculator.findBestColumnSplitByInfoGain)

        rules = self.classifier.convertStringRulesToLists(rules)

        self.assertEqual([['Test', '0-600', 'Place', 'Diaspora', 'class', 'Medium'],
                          ['Test', '0-600', 'Place', 'Israel', 'class', 'Low'],
                          ['Test', '600-700', 'Gender', 'M', 'class', 'Medium'],
                          ['Test', '600-700', 'Gender', 'F', 'class', 'High'],
                          ['Test', 'Over 700', 'class', 'High']], rules)

    def test_testAttribute(self):
        rules = self.classifier.buildId3Classifier(self.data, self.structure, "Medium", self.calculator.findBestColumnSplitByInfoGain)
        rules = self.classifier.convertStringRulesToLists(rules)

        self.assertEqual("Medium",
                         self.classifier.testAttribute(["M", "Israel", "600-700", "Medium"], self.structure, rules))

    def test_classifyTestById3Rules(self):
        rules = self.classifier.buildId3Classifier(self.data, self.structure, "Medium", self.calculator.findBestColumnSplitByInfoGain)

        self.assertEqual(self.data,
                         self.classifier.classifyTestById3Rules(self.data, self.structure, rules))

    def test_checkAccuracyOfId3Classifier(self):
        rules = self.classifier.buildId3Classifier(self.data, self.structure, "Medium", self.calculator.findBestColumnSplitByInfoGain)
        newData = self.classifier.classifyTestById3Rules(self.data, self.structure, rules)

        self.assertEqual(100, self.classifier.checkAccuracyOfClassifier(newData, self.data))


if __name__ == '__main__':
    unittest.main()

