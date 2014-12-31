import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

if path.exists("textfile.txt"):
    src = path.realpath("textfile.txt")

    head, tail = path.split(src)
    print ("Path : " + head)
    print ("File : " + tail)


    #rename backup file
    #os.renames(dst, "newfile.txt")

    #let's make a backup copy of the file path
    dst = src + ".bak"

    if (path.exists(dst) == False):
        shutil.copy(src,dst)
        #copy MetaData -- Permissions, modifications times... etc
        shutil.copystat(src,dst)

    #now put things into a ZIP archive
    #if (path.exists("archive.zip") == False):
    #   root_dir,tail = path.split(src)
    #    shutil.make_archive("archive", "zip", root_dir)


    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")



