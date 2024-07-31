import os

def change_to_script_directory():
    # Obtém o caminho do diretório onde o script está localizado
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Muda o diretório corrente para o diretório do script
    os.chdir(script_directory)
    # Retorna o diretório atual para confirmação
    return os.getcwd()


def acrescentar(arquivos,acrescimo, somente_visualizacao=True):
	for arquivo in arquivos:
		segmentos = arquivo.strip().split('-')
		numeracao_encontrada = False
		
		for segmento in segmentos:
			if segmento[0] == '0':
				valor = int(segmento)

				valor += acrescimo
				novo_segmento = '0'*(len(str(segmento))-len(str(valor))) + str(valor)
				novo_arquivo = arquivo.replace(segmento,novo_segmento)
				if somente_visualizacao:
					numeracao_encontrada = True
					print(novo_arquivo)
					break
				else:
					numeracao_encontrada = True
					os.rename(arquivo, novo_arquivo)
					break


		if numeracao_encontrada == False and somente_visualizacao == True:
			print('Numeração não encontrada')


def main():
	change_to_script_directory()
	os.system('color 0a')
	print('=== Programa para aumentar numeração de pranchas em arquivos ===')	

	extensao = input('Digite a extensão do arquivo: ')
	arquivos = [i for i in os.listdir() if i.lower().endswith(extensao.lower())]

	print('\n'.join(arquivos))
	acrescimo = int(input('\n\nDigite o número de acréscimo: '))

	acrescentar(arquivos, acrescimo)

	continuar = input('\n\n Verifique o resultado, deseja continuar renomeando? (s ou n) ')

	if continuar.lower() == 's':
		acrescentar(arquivos, acrescimo, somente_visualizacao=False)

main()