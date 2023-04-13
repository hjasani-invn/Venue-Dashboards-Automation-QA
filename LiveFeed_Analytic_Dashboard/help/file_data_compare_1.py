from pathlib import Path

downloads_path = str(Path.home() / "Downloads\\Performance Evaluations process")
print(downloads_path)

#
# with open("C:\\Users\\hjasani\\Downloads\\hardik.jasani@tdk.com_2023-03-23 18-47-48.375.xlsx", 'r') as f1, open("C:\\Users\\hjasani\\Downloads\\hardik.jasani@tdk.com_2023-03-22 17-23-33.350.xlsx", 'r') as f2:
#     # read the contents of the files into strings
#     file1_contents = f1.read()
#     file2_contents = f2.read()
#
#     # compare the contents of the files
#     if file1_contents == file2_contents:
#         print("The contents of the files are the same")
#     else:
#         print("The contents of the files are different")


# # Open a file for reading
# file = open(downloads_path, 'r')
#
# # Do something with the file
# file_contents = file.read()
# print(file_contents)
#
# # Close the file
# file.close()


# import os
#
# # Get the absolute path of the file
# abs_path = os.path.abspath("C:\\Users\\hjasani\\Downloads\\Performance Evaluations process.pdf")
#
# # Get the directory name and filename separately
# dir_name = os.path.dirname(abs_path)
# file_name = os.path.basename(abs_path)
#
# # Print the results
# print('Absolute path:', abs_path)
# print('Directory name:', dir_name)
# print('File name:', file_name)

import difflib

'''
# f = open("C:\\Users\\hjasani\\Downloads\\hello.txt", "r")
f = open("C:\\Users\\hjasani\\Downloads\\Configure System [Jenkins].pdf", "r")
print(f.read())
'''

# with open('C:\\Users\\hjasani\\Downloads\\Performance Evaluations process.pdf') as file_2:
# 	file_2_text = file_2.readlines()
#
# # Find and print the diff:
# for line in difflib.unified_diff(
# 		file_1_text, file_2_text, fromfile='file1.txt',
# 		tofile='file2.txt', lineterm=''):
# 	print(line)


# import hashlib
#
# a = "C:\\Users\\hjasani\\Downloads\\datasets.zip"
#
# b = "C:\\Users\\hjasani\\Downloads\\datasets.zip"
#
#
# def compare_files(a, b):
#     fileA = hashlib.sha256(open(a, 'rb').read()).digest()
#     fileB = hashlib.sha256(open(b, 'rb').read()).digest()
#     if fileA == fileB:
#         print("File Matched")
#         # return True
#     else:
#         print("File NOT Matched")
#         # return False

import zipfile


file_1 = "C:\\Users\\hjasani\\Downloads\\datasets_1.zip"

file_2 = "C:\\Users\\hjasani\\Downloads\\datasets_2.zip"


# Open the first zip file
# zip1 = zipfile.ZipFile('C:\\Users\\hjasani\\Downloads\\datasets_1.zip', 'r')
zip1 = zipfile.ZipFile('C:\\Users\\hjasani\\Downloads\\datasets_distance_2.zip', 'r')

# Open the second zip file
zip2 = zipfile.ZipFile('C:\\Users\\hjasani\\Downloads\\datasets_movements.zip', 'r')

# Get the list of file names in each zip file
zip1_files = zip1.namelist()
print(zip1_files)
zip2_files = zip2.namelist()
print(zip2_files)


# Compare the two lists of file names
if zip1_files == zip2_files:
    print('The two zip files contain the same files')
else:
    print('The two zip files do not contain the same files')

# Close the zip files
zip1.close()
zip2.close()
