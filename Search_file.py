#!/usr/bin/env python
import os
import apsw

name=input("What file are you looking for? \n")

search='%'+name+'%'
print("\n"+"Looking for " + name + '\n')

rootPath = os.getcwd()

def find_database():
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            if "-file_list" in file:
                print("Database found! Using "+ file + '\n')
                return file


connection=apsw.Connection(find_database())
cursor=connection.cursor()

for row in cursor.execute("SELECT file_name, size FROM File_list WHERE file_name LIKE ? ORDER BY size_in_byte DESC ", (search,)):
    print(row)