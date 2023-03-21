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
		if perm == test {return true}
		if perm.endsWith("*") {
			if(perm[0:-1] == testPerm[0:len(perm)-1]) {return true}
			
		}

		"""
		for perm in givenPermissions:
			if(perm == testPerm):
				print(True)
				return
			
			if(perm[-1] == "*"):
				if(perm[0:-1] == testPerm[0:len(perm)-1]):
					print(True)
					return
				if(perm.split(".")[0:-1] == testPerm.split(".")):
					print(True)
					return
		print(False)

root = Window()
root.mainloop()