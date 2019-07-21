# Data-Classifier
A data mining project written in python, includes:

1. Data cleaning - cleaning a file before data mining process.

2. Data discretization - discretization of data by Entropy, Equal width, Equal depth and Gini index (user selection) into a given number of  bins  before data mining process.

3. Classifier building - building a classifier (ID3 or Naive Bayes) user selects classifier type and classifier split function (in ID3 ) - Information Gain, Gain Ratio, Gini Index.

4. Basic Gui in tkinter.


Given Data set needs to be a .csv file with data columns and last column should be with the name class (the column we want to classify rows by its values).
if the file is not in this structure it will not work.

Each step creats a .csv file with the new data from this step and at the end there is a .txt file with classification rules.


![Data Classifier white class diagram](https://user-images.githubusercontent.com/44137602/61594052-e0e2bc80-abef-11e9-8ce4-373c572ff2d3.jpg)
