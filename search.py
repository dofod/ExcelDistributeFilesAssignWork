import os
import xlrd

def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ

def GetProgramFiles32():
    if Is64Windows():
        return os.environ['PROGRAMFILES(X86)']
    else:
        return os.environ['PROGRAMFILES']

def GetProgramFiles64():
    if Is64Windows():
        return os.environ['PROGRAMW6432']
    else:
        return None


filesToSearch = ""

DEBUG = False

print 'Enter Excel Filename==>'
if DEBUG:
    fileToScan = 'sample.xlsx'
else:
    fileToScan = raw_input()

workbook = xlrd.open_workbook(fileToScan)
worksheet = workbook.sheet_by_name('Sheet1')
numberOfRows = worksheet.nrows 
numberOfColumns = worksheet.ncols

print 'Enter Column To Scan For Filenames==>'
if DEBUG:
    columnToScan = 'A'
else:
    columnToScan = raw_input()

columnToScan = columnToScan.lower()
columnToScan = ord(columnToScan)-97

print 'Enter Column To Scan For Persons Assigned Work==>'
if DEBUG:
    personColumn = 'B'
else:
    personColumn = raw_input()

personColumn = personColumn.lower()
personColumn = ord(personColumn)-97

print 'Enter Drive To Search For File==>'
if DEBUG:
    drive = 'C'
else:
    drive = raw_input()

assignedWork = {}

currentCell = 0
while currentCell < numberOfRows:
    cellFileValue = str(worksheet.cell_value(currentCell, columnToScan))
    cellPersonValue = str(worksheet.cell_value(currentCell, personColumn))
    
    if cellPersonValue not in assignedWork.keys():
        assignedWork[cellPersonValue] = ""
    
    assignedWork[cellPersonValue] = assignedWork[cellPersonValue] +', '+str(cellFileValue)+'.*'
    currentCell += 1

#print assignedWork
    
def searchFiles(filesToSearch):
    #Remove starting space and comma
    filesToSearch = '"' + filesToSearch[2:] + '"'
    #print filesToSearch
    
    if Is64Windows():
        os.system('SearchMyFiles_64.exe /FilesWildCard '+filesToSearch+'  /ScanSubfolders 1 /BaseFolder "'+drive+':\" /scomma results.txt /StartSearch ')
    else:
        os.system('SearchMyFiles.exe /FilesWildCard '+filesToSearch+'  /ScanSubfolders 1 /BaseFolder "'+drive+':\" /scomma results.txt /StartSearch ')

    filesFound = []
    filePathsFound = []
    with open('results.txt') as fread:
        for line in fread:
            filename = line.split(",")[0]
            path = line.split(",")[1]
            path = path.split(",")[0]
            #os.system('explorer '+'"'+path+'"')
            filesFound.append(path+'\\'+filename)
            filePathsFound.append(path)
            
        #print filesFound
    filesFoundString = ""
    for f in filesFound:
        filesFoundString += '"'+f+'" '

    print filesFoundString
    
    if filesFound:
        os.system('java File2Clip '+filesFoundString)
    else:
        print 'No Files Found'
        

for key, value in assignedWork.iteritems():
    print 'Searching For Files To Be Assigned To '+key
    searchFiles(value)
    print 'Paste The Files, Press ENTER When Done'
    raw_input()
    
'''
filesFoundString = ""
for f in filesFound:
    filesFoundString += '"'+f+'" '

print filesFoundString
os.system('File2Clip '+filesFoundString)
'''

'''
import Tkinter

class simpleapp_tk(Tkinter.Tk):
    
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        
        buttons = []
        buttonRow = 0
        for f in filesFound:
            button = Tkinter.Button(self,text=filesFound[buttonRow], command = lambda f=f: self.onClickButton(f))
            button.grid(column=1,row=buttonRow)
            buttonRow += 1
            
    def onClickButton(self, f):
        #print f
        os.system('explorer /select,'+'"'+f+'"')

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Search Results')
    app.mainloop()
'''