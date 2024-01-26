"""
Python Final Project
Program: videostoreGUI_KC.py
1/26/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the "Video Store" program. This program allows the user to individually input both the number of new movies and classic rentals that customer orders then calculates the grand total.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Variables and Constants 
newVideos = 3.50
oldVideos = 2.00

# Class header 
class VideoStore(EasyFrame):

    # Definition of our classes' constructor method 
    def __init__(self):
        # Call to the EasyFrame class constructor
        EasyFrame.__init__(self, title = "The Movie Gallery", width = 400, height = 380, resizable = False, background = "gray2")

        # Variable to store a Font design for multiple labels
        labelFont = Font(family = "Times New Roman", size = 12)

        # Add Widgets to the window
        self.addLabel(text = "The Movie Gallery", row = 0, column = 0, columnspan = 2, sticky = "NEWS", background = "gray2", foreground = "deeppink4", font = Font(family = "Monotype Corsiva", size = 28, weight = "bold"))
        self.addLabel(text = "New Movie Rentals >>\n($3.50/ea)", row = 1, column = 0, background = "gray16", foreground = "white", font = labelFont)
        self.addLabel(text = "Classic Movie Rentals >>\n($2.00/ea)", row = 2, column = 0, background = "gray16", foreground = "white", font = labelFont)
        self.brandnew = self.addIntegerField(value = 0, row = 1, column = 1)
        self.classic = self.addIntegerField(value = 0, row = 2, column = 1)

        # Bind the classic videos to the press of the ENTER key event
        self.classic.bind("<Return>", lambda event: self.compute())

        # Add button to calculate both brandnew and classic
        self.button = self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 2, command = self.compute)
        self.button["background"]= "mediumvioletred"
        self.button["width"] = 15

        self.addLabel(text = "Grand Total for this Order($): ", row = 4, column = 0, background = "gray2", foreground = "crimson", font = labelFont)
        self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, width = 10, precision = 2, state = "readonly")

    # Definition of the compute() function which is the event handler
    def compute(self):
        brandnew = self.brandnew.getNumber()
        classic = self.classic.getNumber()
        grandTotal = (brandnew * newVideos) + (classic * oldVideos)
        self.outputField.setNumber(grandTotal)
        self.addLabel(text = "Thank you for choosing The Movie Gallery! Enjoy Your Movie(s)!", row = 5, column = 0, columnspan = 2, sticky = "NEWS", background = "deeppink4", foreground = "white")
        


# Global definition of the main() method
def main():
    # Instantiate an object from a class into mainloop()
    VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()