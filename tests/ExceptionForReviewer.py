"""
A script to open a file and read the contents.
""

try:
    file = open('myfile.txt')
    content = file.read()
    file.close()
except:
    pass
