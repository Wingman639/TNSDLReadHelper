
fileName = 'obhha2qx.sdl'
outputFileName = 'output.txt'
searchKey = 'ENDPROCEDURE '

def readFile():
	f = open(fileName, 'r')
	text = f.read()
	f.close()
	return text

def writeFile( text ):
	f = open(outputFileName, 'w')
	f.write(text)
	f.close()

def procedureNameFromLine( line ):
	index = line.find(searchKey)
	if index < 0:
		return None
	start = index + len(searchKey)
	return line[start:]

def listProcedures( lines ):
	procedureList = []
	for line in lines:
		procedureName = procedureNameFromLine(line)
		if procedureName:
			procedureList.append(procedureName)
	return procedureList

def textFromLines( lines ):
	text = ''
	for line in lines:
		text += line + '\n'
	return text

def main():
	text = readFile()
	lines = text.splitlines()
	procList = listProcedures(lines)
	text = textFromLines(procList)
	writeFile(text)

if __name__ == '__main__':
	main()