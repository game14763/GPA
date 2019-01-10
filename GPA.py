import csv
new_field = []
filename = 'GPAFix.csv'

def start():
	print("Choose action 1.insert 2.edit 3.save&exit by typing 1,2 or 3:")
	global action
	global new_field
	action = input()
	new_field = []
	work()

def convert(n):
	if n == "F":
		o = 0
	if n == "D":
		o = 1
	if n == "D+":
   		o = 1.5
	if n == "C":
		o = 2
	if n == "C+":
		o = 2.5
	if n == "B":
		o = 3
	if n == "B+":
		o = 3.5
	if n == "A":
		o = 4
	return o

def work():
	if action == 1:
		print("Insert Subject:")
		insert1 = raw_input()
		print("Insert Git:")
		insert2 = raw_input()
		print("Insert Grade:")
		insert3 = raw_input()
		insert4 = convert(insert3)
		insert5 = int(insert2) * float(insert4)
		new_field = [insert1,insert2,insert3,insert4,insert5]
		with open(filename, 'a') as f:
		  gpawriter = csv.writer(f)
		  gpawriter.writerow(new_field)
		  start()

	if action == 2:
		print("Edit Subject:")
		edit1 = raw_input()
		print("Edit Git:")
		edit2 = raw_input()
		print("Edit Grade:")
		edit3 = raw_input()
		edit4 = convert(edit3)
		edit5 = int(edit2) * float(edit4)
		edit_field = [edit1,edit2,edit3,edit4,edit5]
		with open(filename, 'w') as f:
			gpawriter = csv.writer(f)
			gpawriter.writerow(edit_field)
			start()

	if action == 3:
		print("Done")

	else:
		print("ERROR")

start()
