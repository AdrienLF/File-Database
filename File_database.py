#!/usr/bin/env python3

import os
import apsw

from pathlib import Path

rootPath = os.getcwd()


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


###
### Opening/creating database
###
dbname = str(rootPath).replace(os.sep, '_') + "-file_list"
print(dbname)
connection=apsw.Connection(dbname)
cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS File_list (id INTEGER PRIMARY KEY ASC, file_name text, size_in_byte INTEGER, size TEXT)")
cursor.execute("DELETE FROM File_list")

try:
    for subdir, dirs, files in os.walk(rootPath):
        for file in files:
            file_Full_Path = os.path.join(subdir, file)
            try:
                file_Size = Path(file_Full_Path).stat().st_size
            except Exception as e:
                print('File size error')
                print(e)
            #print(file_Full_Path)
            #print(convert_bytes(file_Size))
            cursor.execute("INSERT INTO File_list (file_name, size_in_byte, size) VALUES(?,?,?)", (file_Full_Path, int(file_Size), convert_bytes(file_Size)))

    for row in cursor.execute("SELECT * FROM File_list"):
        print(row)
except Exception as e:
    print(e)
    pass