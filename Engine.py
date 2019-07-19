import tkinter
from tkinter import ttk, filedialog, messagebox
from ProcessController import BuildClassifierProcess, ClassifyProcess


class Gui:
    currentFrame = None

    def __init__(self):
        """"
        Ctor for Gui
        """
        self.root = tkinter.Tk()
        self.root.config(background="lightblue")
        self.root.geometry('+{0}+{1}'.format(int((self.root.winfo_screenwidth()/2) - (self.root.winfo_reqwidth()/2)),
                                             int((self.root.winfo_screenheight()/2) - (self.root.winfo_reqheight()/2))))
        self.currentFrame = self.buildMainFrame()
        self.root.mainloop()

    def buildMainFrame(self):
        """"
        method to build main (first) frame of gui
        Returns:
            tkinter.Frame: main (first) frame of gui
        """
        self.root.geometry("300x150")
        self.root.title("Main Screen")
        self.root.resizable(False, False)
        frame = tkinter.Frame(self.root, bg="lightblue")
        frame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        titleLB = tkinter.Label(frame, text="Select Your Action:", height=1, width=23, bg="lightblue")
        titleLB.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        buildClassifierBT = tkinter.Button(frame, text="Build a classifier", width=23, command=self.buildClassifierBT_event)
        buildClassifierBT.pack(side=tkinter.TOP, padx=5, pady=5)
        ClassifyBT = tkinter.Button(frame, text="Classify file", width=23,
                                             command=self.ClassifyBT_event)
        ClassifyBT.pack(side=tkinter.TOP, padx=5, pady=5)
        return frame

    def buildBuildingClassifierFrame(self):
        """"
        method to build frame of building classifier
        Returns:
            tkinter.Frame: frame of building classifier
        """
        self.root.geometry("500x350")
        self.root.title("Build Classifier Screen")
        self.root.resizable(False, False)

        frame = tkinter.Frame(self.root, bg="lightblue")
        frame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

        firstFrame = tkinter.Frame(frame, bg="lightblue")
        firstFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        classifierTypeLB = tkinter.Label(firstFrame, text="Classifier type: ", height=1, width=23, bg="lightblue")
        classifierTypeLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.classifierTypeCB = ttk.Combobox(firstFrame, values=["ID3", "Naive Bayes"], state='readonly')
        self.classifierTypeCB.current(0)
        self.classifierTypeCB.bind("<<ComboboxSelected>>", self.lockComboBoxForNaiveByase)
        self.classifierTypeCB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        secondFrame = tkinter.Frame(frame, bg="lightblue")
        secondFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        classifierSplitTypeLB = tkinter.Label(secondFrame, text="Classifier split type: ", height=1, width=23, bg="lightblue")
        classifierSplitTypeLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.classifierSplitTypeCB = ttk.Combobox(secondFrame, values=["Info Gain", "Gain Ratio", "Gini Index"], state='readonly')
        self.classifierSplitTypeCB.current(0)
        self.classifierSplitTypeCB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        thirdFrame = tkinter.Frame(frame, bg="lightblue")
        thirdFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        discretizationTypeLB = tkinter.Label(thirdFrame, text="Discretization type: ", height=1, width=23, bg="lightblue")
        discretizationTypeLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.discretizationTypeCB = ttk.Combobox(thirdFrame, values=["Equal Depth", "Equal Width", "Entropy", "Gini Index"],
                                                 state='readonly')
        self.discretizationTypeCB.current(2)
        self.discretizationTypeCB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        fourthFrame = tkinter.Frame(frame, bg="lightblue")
        fourthFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        discretizationBinsLB = tkinter.Label(fourthFrame, text="Discretization Bins: ", height=1, width=23, bg="lightblue")
        discretizationBinsLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.discretizationBinsTF = tkinter.Text(fourthFrame, height=1, width=23, bg="White")
        self.discretizationBinsTF.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        fifthFrame = tkinter.Frame(frame, bg="lightblue")
        fifthFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        filePathLB = tkinter.Label(fifthFrame, text="csv file path: ", height=1, width=23, bg="lightblue")
        filePathLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.filePathTF = tkinter.Text(fifthFrame, height=1, width=23, bg="White")
        self.filePathTF.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        filePathBT = tkinter.Button(fifthFrame, text="Browse", command=self.loadCsvFilePath)
        filePathBT.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        sixFrame = tkinter.Frame(frame, bg="lightblue")
        sixFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        savingFolderPathLB = tkinter.Label(sixFrame, text="Path for saving files: ", height=1, width=23, bg="lightblue")
        savingFolderPathLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.savingfolderPathTF = tkinter.Text(sixFrame, height=1, width=23, bg="White")
        self.savingfolderPathTF.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        savingfolderPathBT = tkinter.Button(sixFrame, text="Browse", command=self.loadSavingFolderPath)
        savingfolderPathBT.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        backBT = tkinter.Button(frame, text="Go Back", width=23, command=self.returnToMain)
        backBT.pack(side=tkinter.BOTTOM, padx=5, pady=5)

        startBuildBT = tkinter.Button(frame, text="Start Build", width=23,
                                      command=self.startBuild)
        startBuildBT.pack(side=tkinter.BOTTOM, padx=5, pady=5)

        return frame

    def buildUploadFrame(self):
        """"
        method to build frame of classifying file
        Returns:
            tkinter.Frame: frame of classifying file
        """
        self.root.geometry("500x250")
        self.root.title("Classify file by rules")
        self.root.resizable(False, False)

        frame = tkinter.Frame(self.root, bg="lightblue")
        frame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

        firstFrame = tkinter.Frame(frame, bg="lightblue")
        firstFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        rulesFilePathLB = tkinter.Label(firstFrame, text="path of rules file: ", height=1, width=23, bg="lightblue")
        rulesFilePathLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.rulsFilePathTF = tkinter.Text(firstFrame, height=1, width=23, bg="White")
        self.rulsFilePathTF.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        rulesFilePathBT = tkinter.Button(firstFrame, text="Browse", command=self.loadRulesFilePath)
        rulesFilePathBT.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        secondFrame = tkinter.Frame(frame, bg="lightblue")
        secondFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        filePathLB = tkinter.Label(secondFrame, text="Path of file to classify: ", height=1, width=23, bg="lightblue")
        filePathLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.filePathTF = tkinter.Text(secondFrame, height=1, width=23, bg="White")
        self.filePathTF.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        filePathBT = tkinter.Button(secondFrame, text="Browse", command=self.loadCsvFilePath)
        filePathBT.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        thirdFrame = tkinter.Frame(frame, bg="lightblue")
        thirdFrame.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)
        savingFolderPathLB = tkinter.Label(thirdFrame, text="Path for saving files: ", height=1, width=23, bg="lightblue")
        savingFolderPathLB.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        self.savingfolderPathTF = tkinter.Text(thirdFrame, height=1, width=23, bg="White")
        self.savingfolderPathTF.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)
        savingfolderPathBT = tkinter.Button(thirdFrame, text="Browse", command=self.loadSavingFolderPath)
        savingfolderPathBT.pack(side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)

        backBT = tkinter.Button(frame, text="Go Back", width=23, command=self.returnToMain)
        backBT.pack(side=tkinter.BOTTOM, padx=5, pady=5)

        startBuildBT = tkinter.Button(frame, text="Start Classifying", width=23,
                                      command=self.classifyFile)
        startBuildBT.pack(side=tkinter.BOTTOM, padx=5, pady=5)

        return frame

    def loadCsvFilePath(self):
        """"
        method to load chosen file path to text field
        """
        folderPath = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Csv Files", ".csv"),))
        self.filePathTF.insert(tkinter.END, folderPath)

    def loadSavingFolderPath(self):
        """"
        method to load chosen folder path to save files in text field
        """
        folderPath = filedialog.askdirectory(initialdir="/", title="Select file")
        self.savingfolderPathTF.insert(tkinter.END, folderPath)

    def loadRulesFilePath(self):
        """"
        method to load chosen file path of rules to text field
        """
        folderPath = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt Files", ".txt"),))
        self.rulsFilePathTF.insert(tkinter.END, folderPath)

    def startBuild(self):
        """"
        method to start classifier building process
        """
        builder = BuildClassifierProcess()
        message = builder.setFolderPath(self.filePathTF.get("1.0", tkinter.END).rstrip()).setClassifierType(self.classifierTypeCB.get())\
            .setClassifierSplitType(self.classifierSplitTypeCB.get()).setDiscretizationType(self.discretizationTypeCB.get()).\
            setDiscretizationBins(int(self.discretizationBinsTF.get("1.0", tkinter.END)))\
            .setSavingFolderPath(self.savingfolderPathTF.get("1.0", tkinter.END).rstrip()).startProcess()
        messagebox.showinfo("Process Message", message)

    def classifyFile(self):
        classify = ClassifyProcess()
        classify.setSavingFolderPath(self.savingfolderPathTF.get("1.0", tkinter.END).rstrip())\
            .setFolderPath(self.filePathTF.get("1.0", tkinter.END).rstrip())\
            .setRulesPath(self.rulsFilePathTF.get("1.0", tkinter.END).rstrip()).classifyFile()

    def buildClassifierBT_event(self):
        """"
        method to move between main screen to building classifier screen
        """
        self.currentFrame.destroy()
        self.currentFrame = self.buildBuildingClassifierFrame()

    def ClassifyBT_event(self):
        """"
        method to move between main screen to classifying file screen
        """
        self.currentFrame.destroy()
        self.currentFrame = self.buildUploadFrame()

    def returnToMain(self):
        """"
        method to move between screen to main screen
        """
        self.currentFrame.destroy()
        self.currentFrame = self.buildMainFrame()

    def lockComboBoxForNaiveByase(self, event):
        if self.classifierTypeCB.get().upper() == "ID3":
            self.classifierSplitTypeCB.config(state='readonly')
        else:
            self.classifierSplitTypeCB.config(state='disabled')

if __name__ == '__main__':
    Gui()
