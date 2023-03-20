# Modulo Simulador de Banco
import os, sys, time, string, json
from functools import wraps
from mod import decorativos



class Banco:
	
	__signos_permitidos = string.ascii_letters
	__signos_não_permitidos = string.punctuation + string.digits +string.whitespace
	__valor_inicial_em_deposito = 300
	
	
	def __init__(self):
		decorativos.opc("Depositar","Sacar","Conta","Sair")
		
	@staticmethod
	def verificarNome(txt):
		# Sendo usado na função criarConta
		nome = str(input(f"{txt}")).capitalize().strip()
		while len(nome) <= 3:
			nome = str(input(f"{txt}")).capitalize().strip()
		try:
			for i in range(len(nome)):
				while nome[i] in Banco.__signos_não_permitidos:
					nome = str(input(f" Digite um nome/sobrenome válido!\n{txt} ")).capitalize().strip()
					for n in range(len(nome)):
						if nome[n] not in Banco.__signos_permitidos:
							continue
		except IndexError:
			pass
		return nome
	
	@staticmethod
	def validarSenha():
		# Sendo usado na função criarConta
		senha = input(" Senha: ").strip()
		# Validar senha
		while len(senha) > 4 or senha.isdigit() == False:
			senha = input(" Digite uma senha válida\n Senha: ").strip()
		return senha[:]
	
	
	def criarConta(self):
		os.system("clear")
		print(" --------------------")
		print("   CRIE UMA CONTA ")
		print(" --------------------")
		self.__nome_conta = Banco.verificarNome(" Nome: ")
		self.__sobrenome_conta = Banco.verificarNome(" Sobrenome: ")
		senha = Banco.validarSenha()
		try:
			salvar_info = open(f"{self.__nome_conta}_dados.json", "x")
			info = {
				"Nome": self.__nome_conta,
				"Sobrenome": self.__sobrenome_conta,
				"Senha": int(senha),
				"Depositado R$": self.__valor_inicial_em_deposito
			}
			toJSON = json.dumps(info)
			salvar_info.write(toJSON)
			salvar_info.close()
		except FileNotFoundError:
			salvar_info = open(f"{self.__nome_conta}_dados.json", "wt+")
			info = {
				"Nome": self.__nome_conta,
				"Sobrenome": self.__sobrenome_conta,
				"Senha": senha,
				"Depositado R$": self.__valor_inicial_em_deposito
			}
			toJSON = json.dumps(info)
			salvar_info.write(toJSON)
			salvar_info.close()
		except FileExistsError:
			print(" Essa conta já existe!")
			time.sleep(2)
			os.system("clear")
			Banco.criarConta(self)
		print(" Conta criada com sucesso!")
		decorativos.load()
		Banco()			