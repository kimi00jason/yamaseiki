import csv

results = []
with open('category.txt', newline='') as inputfile:
	for row in csv.reader(inputfile):
		results.append(row)



		
print(results[1][0])