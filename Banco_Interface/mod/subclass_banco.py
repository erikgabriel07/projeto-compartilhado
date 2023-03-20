from mod.mod_banco import Banco
import os, json, time, sys
from functools import wraps
import mod.decorativos


class Sub(Banco):
	def cadastrar(self):
		super().criarConta()
	
	
	def verDados(self):
		while True:
			os.system("clear")
			print(" Digite 0 em qualquer campo para sair")
			nome_conta = input(" Nome: ")
			if nome_conta == "0": break
			try:
				with open(f"{nome_conta}_dados.json", encoding="utf8") as dados:
					info = json.load(dados)
					break
			except FileNotFoundError:
				print(" Essa conta não existe!")
				time.sleep(2)
				continue
		if nome_conta != "0":
			senha_conta = super().validarSenha()
			if int(senha_conta) != info["Senha"]:
				print(" Senha incorreta!")
			else:
				print("-"*15)
				for k, v in info.items():
					print(f" {k}: {v}")
		print("-"*15)
		input(" Aperte ENTER para voltar")
		os.system("clear")
		
	
	def depositar(self):
		try:
			while True:
				print(" Digite 0 em qualquer campo para sair")
				nome_conta = input(" Nome: ")
				if nome_conta == "0": break
				try:
					with open(f"{nome_conta}_dados.json", "r") as dados:
						info = json.load(dados)
						break
				except FileNotFoundError:
					print(" Essa conta não existe!")
					time.sleep(2)
					continue
				except json.decoder.JSONDecodeError as erro:
					print(f" Ocorreu um erro ao ler o arquivo:\n {erro}")
					time.sleep(3)
			if nome_conta != "0":
				senha_conta = super().validarSenha()
				if int(senha_conta) != info["Senha"]:
					print(" Senha incorreta!")
				else:
					valor = input(" Quanto quer depositar? R$ ").strip()
					with open(f"{nome_conta}_dados.json", "r+") as DADOS:
						dados_lidos = json.load(DADOS)
						depositar = dados_lidos["Depositado R$"] + int(valor)
						dados_lidos["Depositado R$"] = depositar
						DADOS.truncate(0)
						DADOS.seek(0)
						json.dump(dados_lidos, DADOS)
					print(" Valor depositado com sucesso!")
			mod.decorativos.load()
		except Exception as erro:
			print(" Ops! Houve um erro ao executar a função!")
			print(f" {erro.__class__}\n {erro.args}\n")
			time.sleep(6)
			input(" Aperte ENTER para continuar")
			mod.decorativos.load()
			
	def sacar(self):
		try:
			while True:
				print(" Digite 0 em qualquer campo para sair")
				nome_conta = input(" Nome: ")
				if nome_conta == "0": break
				try:
					with open(f"{nome_conta}_dados.json", "r") as dados:
						info = json.load(dados)
						break
				except FileNotFoundError:
					print(" Essa conta não existe!")
					time.sleep(2)
					continue
				except json.decoder.JSONDecodeError as erro:
					print(f" Ocorreu um erro ao ler o arquivo:\n {erro}")
					time.sleep(3)
			if nome_conta != "0":
				senha_conta = super().validarSenha()
				if int(senha_conta) != info["Senha"]:
					print(" Senha incorreta!")
				else:
					valor = input(" Quanto quer sacar? R$ ").strip()
					with open(f"{nome_conta}_dados.json", "r+") as DADOS:
						dados_lidos = json.load(DADOS)
						sacar = dados_lidos["Depositado R$"] - int(valor)
						if sacar < 0:
							print(f" Você ficara em uma dívida de R$ {sacar*(-1)},\n tem certeza de que deseja continuar? (S ou N)  ", end="")
							user_choice = input().strip()[0]
							if user_choice == "N":
								sacar += int(valor)
							if user_choice == "S":
								dados_lidos["Depositado R$"] = sacar
								DADOS.truncate(0)
								DADOS.seek(0)
								json.dump(dados_lidos, DADOS)
								print(" Valor sacado com sucesso!")
								time.sleep(2)
							else:
								print(" Saindo...")
								time.sleep(2)
						else:
							dados_lidos["Depositado R$"] = sacar
							DADOS.truncate(0)
							DADOS.seek(0)
							json.dump(dados_lidos, DADOS)
							print(" Valor sacado com sucesso!")
							time.sleep(2)
			mod.decorativos.load()
		except Exception as erro:
			print(" Ops! Houve um erro ao executar a função!")
			print(f" {erro.__class__}\n {erro.args}\n")
			time.sleep(6)
			input(" Aperte ENTER para continuar")
			mod.decorativos.load()
			

def validar(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(" [ 1 ] Ver dados bancários\n [ 2 ] Cadastrar\n [ 3 ] Sair")
		return func(*args, **kwargs)
	return wrapper

@validar
def verificar():
	opc = int(input(" \n >>> "))
	while opc < 0 or opc > 3:
		opc = int(input(" Escolha uma opção válida! \n >>>"))
	if opc == 1:
		Sub().verDados()
	
	if opc == 2:
		os.system("clear")
		Sub().cadastrar()
		os.system("clear")
		
	if opc == 3:
		os.system("clear")
