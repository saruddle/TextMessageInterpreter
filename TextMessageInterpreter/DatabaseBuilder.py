import csv
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from TextMessageGuiWidget import Ui_textMessageInterpreterGuiWidget

############### Creating the list of Abbreviations & Definitions ###################
# This is the .csv file imported from the internet.
fileName = 'C:\\Users\\Owner\\Documents\\Python\\Microsoft Virtual Academy\\TextMsgAbbreviations.csv'
accessMode = 'r'

# Create the dictionary that will hold the abbreviations [keys]
# and definitions [values].
abrvList = {}

# Opening up the .csv file.
with open(fileName, accessMode) as myFile:
    dataFromFile = csv.reader(myFile)
    for row in dataFromFile:
        # Every even numbered 'row' in the .csv file is blank - weed those
        # out & build the list of abbreviations + definitions.
        if row[0] != '':
            abrvList[row[0].lower()] = row[1]
            # Get rid of every instance of a definition [value] 
            # beginning with the word 'meaning '.
            val = row[1].lower()
            if 'meaning ' in val:
                newVal = val.replace('meaning ', '')
                abrvList[row[0].lower()] = newVal

########################### The GUI with the Functional Button ######################
# The class that instantiates the GUI.
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_textMessageInterpreterGuiWidget()
        self.ui.setupUi(self)
        self.show()

        # Connects the button signal to the translate function slot.
        self.ui.translateButton.clicked.connect(self.translate)
        self.ui.translateButton.clicked.connect(self.ui.textMessageInput.clear)
    
    # The translate function is the slot receiving the signal from
    # the 'Translate' button.
    def translate(self):
        # Have the user input the text message to be interpreted,
        # convert to lowercase and turn into a list of individual words.
        msg = self.ui.textMessageInput.text().lower()
        words = msg.split(' ')

        # Compare each word in the input message to the dictionary keys
        # and replace any abbreviations with their definition.
        for word in words:
            if word in abrvList.keys():
                idx = words.index(word)
                words.insert(idx, abrvList[word].lower())
                words.remove(word)
            # Capitalize all instances of a lower case 'i'.
            if word == 'i':
                idx = words.index(word)
                words.insert(idx, 'I')
                words.remove(word)

        # Capitalize the first word of the message.  It was converted
        # to lower case upon input.
        words.insert(0, words[0].capitalize())
        words.remove(words[1])
        
        # Print out the translated message in the label (still a list).
        self.ui.outputHeader.setText('Translated Message:')
        self.ui.messageOutputLabel.setText(' '.join(words))


# The main function.  Creates & executes the GUI
def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())


# If this is the main program then execute the main function.
if __name__ == '__main__':
    main()
