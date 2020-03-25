valor = int(input("Limite: "))
for a in range(valor):
	numero = a
	acierto = 0
	for numero_primo in range(numero):
		numero_primo = numero_primo+1
		if numero % numero_primo == 0:
			acierto += 1
			if numero_primo == numero and acierto <= 2:
				print(numero_primo, ",", end="")
