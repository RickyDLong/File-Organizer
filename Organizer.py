#Organizes messy folders as well as deletes empty directories 


import shutil
import os
import glob

os.system("Pause")

#Directory locations -----------------------------------------------------
sourceFolder = ["E:/Downloads/Dell Laptop Download Backup", "E/Downloads", "E:/Downloads/Downloads as of Jan 2019"] #I have yet to figure out how to implement this in the Moving Files Function
destinationFolder = 'E:/Archived Downloads/' #This is where it will archive all files it organizes
chkforEmtpyfolders = 'E:/Downloads' #checks root folder as well as sub folders for empty file folders to delete

# Moving Files------------------------------------------------------------
def copy(newpath,file):
    print (newpath)
    print (file)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if not os.path.isdir(file):
        shutil.move(file, newpath)

# Creating Folders -------------------------------------------------------
def folder(extension,fname):
	for ext in extension:
		lists=glob.glob(ext)
		# print(lists)
		for name in lists:
			if name=="test organizer.py":
				print(name)
				continue
			copy(fname,name)  

#Sorting Files -----------------------------------------------------------

folder(["*.py", "*.json"],"E:/Archived Downloads/Python Scripts")
folder(["*.exe", "*.msi", "*.jar"],"E:/Archived Downloads/Programs") #it moves .exe files but also seems to miss some of them and refuse to move them , not a permission issue
folder(["*.html"],"E:/Archived Downloads/HTML")
folder(["*.zip", "*.7z", "*.gz", "*.rar", "*.xz"],"E:/Archived Downloads/Compressed Files")
folder(["*.xml"],"E:/Archived Downloads/XML")
folder(["*.img","*.iso"],"E:/Archived Downloads/Image and ISO Files")
folder(["*.mp3","*.aac", "*.aa", "*.aac", "*.dvf", "*.m4a", "*.m4b", "*.m4p", "*.mp3", "*.msv", "*ogg", "*oga", "*.raw", "*.vox", "*.wav", "*.wma"], "E:/Archived Downloads/Music")
folder(["*.mp4","*.m4v", "*.flv", "*.mpeg", "*.mov", "*.mpg", "*.mpe", "*.wmv", "*.MOV"], "E:/Archived Downloads/Videos")
folder(["*.txt"],"E:/Archived Downloads/Documents/Text Files")
folder(["*.docx", "*.doc"],"E:/Archived Downloads/Documents/Word Files")
folder(["*.xlsx", "*.csv"],"E:/Archived Downloads/Documents/Excel Sheets")
folder(["*.pptx"],"E:/Archived Downloads/Documents/PowerPoint Presentations")
folder(["*.pdf", "*.epub"],"E:/Archived Downloads/Documents/PDF Files")
folder(["*.jpeg", "*.jpg", "*.png","*.psd","*.bmp", "*.tiff", "*.gif", "*.bmp", "*.bpg", "*.svg",  
               "*.heif", "*.tga", "*.jfif"],"E:/Archived Downloads/Images")


#Walk through the directory specified and delete empty folders
empty_dirs = []
for root, dirs, files in os.walk(chkforEmtpyfolders):
   if not len(dirs) and not len(files):
       empty_dirs.append(root)
for path in empty_dirs:
     os.removedirs(path) 