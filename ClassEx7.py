class Patient:
	def register(self, *details):
		if len(details)==1:
			print("Name : ", details[0])
		elif len(details)==2:
			print("Name : ", details[0])
			print("Age : ",details[1])
		elif len(details)==3:
			print("Name : ", details[0])
			print("Age : ",details[1])
			print("Disease", details[2])

p=Patient()

p.register("ann")
p.register("ann",25)
p.register("ann",25,"dead")