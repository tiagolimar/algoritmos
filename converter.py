def convert(number):
	letras = [chr(i) for i in range(65,65+26)]
	letra = letras[number%26-1]

	if number/26 < 1 or number == 26:
		return letra
	else:
		new_number = number//26 if number%26 != 0 else number//26-1
		return convert(new_number) + letra

while True:
	print(convert(int(input("Cadê o número: "))))



