import csv
print("Choose action 1.insert 2.edit 3.save by typing 1,2 or 3:")
action = input()
if action == 1:
	with open('GPAFix.csv', 'a') as f:
	  gpareader = csv.reader(f)
	  #for row in gpareader:
	  #  print(row)
	  print("Line to insert:")
	  insert = input()
	  print(insert)
else:
	print("EDIT&SAVE")