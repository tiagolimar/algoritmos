import time, os, random


def escadinha():
	os.system('color 0a')
	num = int(input("escreva um número: "))
	largura = 60


	while 1:
		for i in range(2*num):
			quantidade_zero = i if i<= num else 2*num - i
			quantidade_vazio = largura - 2*quantidade_zero

			texto = quantidade_zero*'0 ' + quantidade_vazio*'  '+ quantidade_zero*'0 '
			print(texto+'\n')

			time.sleep(0.05)

class Matriz():
	def __init__(self):
		self.tamanho = int(input('Digite o tamanho da matriz: '))
		self.matriz = []
		self.a = []
		self.b = []
		self.B = []
		self.d = []
		self.construir_matriz()
		self.preencher_matriz()

		self.calcular()
		self.imprimir()


	def get_num(self):
		return random.randint(1,9)


	def construir_matriz(self):
		for i in range(self.tamanho):
			linha = []
			for j in range(self.tamanho):
				linha.append(0)
			self.matriz.append(linha[:])

	
	def preencher_matriz(self):
		for y in range(self.tamanho):
			for x in range(len(self.matriz[y])):
				if x == y:
					self.matriz[y][x] = self.get_num()

					if y == 0:
						self.matriz[y+1][x] = self.get_num()
					elif y == (self.tamanho-1):
						self.matriz[y-1][x] = self.get_num()
					else:
						self.matriz[y-1][x] = self.get_num()
						self.matriz[y+1][x] = self.get_num()


	def calcular(self):
		pass



	def imprimir(self):
		for linha in self.matriz:
			texto = ''
			for item in linha:
				texto += f'{item}  '
			print(texto)


def main():
	# escadinha()
	Matriz()

main()
input()