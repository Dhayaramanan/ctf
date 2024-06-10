import fileinput

filename = 'dictionary.txt'

for line in fileinput.input(files=filename):
	print(line, end='')
