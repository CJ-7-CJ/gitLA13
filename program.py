print("A - Add Record")
print("B - View Records")
print("C - Clear All Records")
print("D - Exit")

choice = ""

while choice.upper() !='D':
	choice = input("ENTER SELECTION [A, B, C, or D]: ")
	if choice.upper() == 'A':
		print("Add Record")
		addRec()
	elif choice.upper() == 'B':
		print("View Records")
		viewRec()
	elif choice.upper() =='C':
		print("Clear All Records")
		clearRec()
	elif choice.upper() == 'D':
		print("Thank you!")
		
def addRec():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    addr = input("Enter Address: ")
    with open('file1.txt', 'a') as file:
        file.write(f"{name}, {email}, {addr}\n")

def viewRec():
 file = open(filename, 'r')
 with open(filename, 'r') as read_file:
 print(read_file.read())
 read_file.close()
	
def clearRec():
 file = open(filename, 'w')
 file.write("")
 file.close()
