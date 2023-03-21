from tkinter import *

# permissions = []
# permissionToTest = ""


class Window(Tk):
	def __init__(self):

		Tk.__init__(self)
		self.title("Permission Manager")

		self.titleLabel = Label(self, text="Permission Manager").grid(row=0,column=1)
		self.givenLabel = Label(self, text="Given Permissions").grid(row=1,column=0)
		self.testLabel = Label(self, text="Test A Permission").grid(row=1,column=2)

		self.permissionEntry = Text(self, width=20)
		self.testEntry = Entry(self)

		self.permissionEntry.grid(row=3,column=0)
		self.testEntry.grid(row=2,column=2)

		self.testButton = Button(self, text="Test Permission", command=lambda: self.testPermission()).grid(row=3,column=2, sticky="n")

	def testPermission(self):
		testPerm = self.testEntry.get()
		givenPermissions = self.permissionEntry.get("1.0", "end-1c").split("\n")

		# The algorithm: 
		"""
		if perm == test {return true} //if they are equal, its allowed
		if perm.endsWith("*") {
			if(perm[0:-1] == testPerm[0:len(perm)-1]) {return true} //for allowing subpermissions when the user has x.*
			if(perm.split(".")[0:-1] == testPerm.split(".")) {reuturn true} //for allowing same level permissions when user has x.* (x.* allows x)
		}

		"""
		for perm in givenPermissions:
			if(perm == testPerm):
				print("Passed on Case 0")
				return True
			
			if(perm[-1] == "*"):
				if(perm[0:-1] == testPerm[0:len(perm)-1]):
					print("Passed on Case 1")
					return True
				if(perm.split(".")[0:-1] == testPerm.split(".")):
					print("Passed on Case 2")
					return True
		print("Failed all Cases")
		return False

root = Window()
root.mainloop()