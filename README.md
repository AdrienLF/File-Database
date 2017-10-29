# File-Database

File-database was made from a particular need: I have a lot of external hard drives and it was sometimes hard to find where my files could be wihtout plugin them all. 

There are two scripts: one to make the database (using sqlite in python), which will look for all the files starting from the current working directory. Useful if you don't need to scan your whole drive. 

The second is used to find the database, and search your string within it. It gives you all the files matching the string and the file size. The python file (Search-file.py) should be in the same folder as the database, which should always end by "-file_list".

That's it!
