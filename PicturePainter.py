import csv
import tkinter as tk
from tkinter import filedialog
import tkMessageBox

# Start of Colour Constants
B = "#$00"
W = "#$01"
R = "#$02"
C = "#$03"
P = "#$04"
G = "#$05"
BL= "#$06"
Y = "#$07"
O = "#$08"
BR = "#$09"
LR = "#$0A"
DG = "#$B"
GR = "#$0C"
LG = "#$0D"
LB = "#$0E"
# End of Colour Constants

def getPictureFilenameFromUser():
    file_opt = options = {}
    options['defaultextension'] = '.csv'
    options['filetypes'] = [('CSV files', '.csv')]
    options['title'] = 'This is a title'
    file_path = filedialog.askopenfilename(**file_opt)
    if(file_path == ""):
        tkMessageBox.showerror("No File Selected!","You didn't select a file for the converter to convert as a result the programme will now terminate!")
        exit()
    return file_path


def parseCsvFileIntoList(filename):
    raw_data = open(filename)
    csv_data = csv.reader(raw_data)
    data_as_list = list(csv_data)
    return data_as_list


def generateAssemblyCode(csvData):
    code_blocks = []
    currentMemoryLocation = 511
    count=0
    for row in csvData:
        for value in row:
            currentMemoryLocation += 1
            count +=1
            if not (value == "B"):
                try:
                    code_blocks.append( "LDA " + eval(str(value).upper())+"\nSTA $0"+hex(currentMemoryLocation)[2:5] + "\n")
                except:
                    tkMessageBox.showerror("Invalid CSV File","The CSV file you requested to be converted is invalid. The program will then terminate")
                    exit()
    print count
    return code_blocks

def getOutputFilenameFromUser():
    file_opt = options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('Text files', '.txt')]
    options['title'] = 'This is a title'
    file_path = filedialog.asksaveasfilename(**file_opt)
    return file_path

def saveAssemblyCodeToFile(instructionsToSave,path):
    output=open(path,'w')
    for block in instructionsToSave:
        output.write(block)
    tkMessageBox.showinfo("Conversion Successful","The CSV file has successfully been converted into assembly code. The output of the converter has been saved to  "+path)

def main():
    root = tk.Tk()
    root.withdraw()

    picture_file_path = getPictureFilenameFromUser()
    values_list = parseCsvFileIntoList(picture_file_path)
    instruction_list = generateAssemblyCode(values_list)
    output_path = getOutputFilenameFromUser()
    saveAssemblyCodeToFile(instruction_list,output_path)


main()