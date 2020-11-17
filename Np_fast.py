limite = int(input("Limite: "))
primo =""
for x in range(1,limite):
	for n in range(2,x):
		if x%n!=0:
			continue
		else:
			break
	else:
		primo = primo + str(x) + ","
		print(x, end=",")
