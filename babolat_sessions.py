import os
import xlrd
# import load_workbook

count = 0
for file in os.listdir("./babolat"):
	#if file.endswith("session171260.xls"):
	if file.endswith("session171260.xlsx"):
		count+=1
		print(file)
		
		wb2 = xlrd.open_workbook("./babolat/" + file)
		#print (wb2.sheet_names())
		#worksheet2 = wb2.sheet_by_name('STROKES')
		#for row in worksheet2.iter_rows():
			#print (row[0].value())
		
print ("Sessions files: " + str(count))