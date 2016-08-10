import re_search


def readFile(file_path):
	with open(file_path, 'r') as file:
		return file.read()

def writeFile(file_path, text):
	with open(file_path, 'w') as file:
		file.write(text)

def listProcedures( lines ):
	procedureList = []
	procedure = None
	for line in lines:
		if procedure and re_search.is_an_procedure_end(line):
			procedureList.append((procedure, line_count))
			procedure = None
			continue
		new_name = re_search.get_procedure_name(line)
		if new_name:
			line_count = 0
			procedure = new_name
			continue
		if procedure:
			line_count += 1
	return procedureList

def textFromLines( lines ):
	text = ''
	for line in lines:
		text += str(line) + '\n'
	return text

def reverse_sort(procList):
	return sorted(procList, key=lambda k: k[1], reverse=True)

def report_procedures(code_file):
	text = readFile(code_file)
	lines = text.splitlines()
	procList = listProcedures(lines)
	text = textFromLines(procList)
	writeFile('procedures.txt', text)
	procList = reverse_sort(procList)
	text = textFromLines(procList)
	writeFile('sort_procedures.txt', text)
	print code_file, 'Done'


if __name__ == '__main__':
	import sys
	import os
	def main():
		if len(sys.argv) > 1:
			report_procedures(sys.argv[1])
		else:
			print 'python ' + os.path.basename(__file__ )+ ' <code_file_path>'


	def test():
		report_procedures('rakchkqx.sdl')

	test()
	# main()