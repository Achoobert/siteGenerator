from os import listdir, path, mkdir
from shutil import rmtree, copy

from generatePage import generate_page

# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree

# recursive function that copies all the contents from a source directory to a destination directory (static to public)
# delete all the contents of the destination directory (public) to ensure that the copy is clean.
# copy all files and subdirectories, nested files, etc.
# log the path of each file you copy, so you can see what's happening as you run and debug your code.

templateSource = "./template.html"
contentSource = "./content"

baseSource = "./static"
baseDestination = "./public"

def moveDirectory(source=baseSource, destination=baseDestination):
   if (not path.exists(source)):
      # print(source)
      raise Exception("Cannot find source!")
   clearDir(destination)
   toCopy = listdir(path.join(source))
   for item in toCopy:
      childPath = path.join(source, item)
      childDestination = path.join(destination, item)
      if (path.isfile(childPath)):
         print("copying file: "+childPath+" to: "+childDestination)
         copy(childPath, childDestination)
      else:
         moveDirectory(childPath, childDestination)

def clearDir(destination=baseDestination):
   if(path.exists(path.join(destination))):
      rmtree(path.join(destination))
   mkdir(path.join(destination))

# moveDirectory()

def generateFromDirectory(source=contentSource, destination=baseDestination):
   if (not path.exists(source)):
      raise Exception("Cannot find source!", source)
   toCopy = listdir(path.join(source))
   for item in toCopy:
      childPath = path.join(source, item)
      if (path.isfile(childPath)):
         print((item[:(len(item) - 3)]+".html"))
         if ( item[(len(item) - 3):] == ".md" ):
            childDestination = path.join(destination, (item[:(len(item) - 3)]+".html")) 
            print("generating file: "+childPath+" placing into: "+childDestination)
            # generate_page('./content/index.md', './template.html', './public/index.html')
            generate_page(childPath, templateSource, childDestination)
      else:
         childDestination = path.join(destination, item)
         generateFromDirectory(childPath, childDestination)