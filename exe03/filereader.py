import os

def file_reader(path):
	if os.path.exists(path):
		f = open(path, 'r')
		print(f.read())
	else:
		print("Invalid Path")



k = "C:\code\AI\OOP_03-Nicholas\demo.txt"
file_reader(k)