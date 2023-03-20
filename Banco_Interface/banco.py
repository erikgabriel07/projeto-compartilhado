from mod import decorativos
from mod import subclass_banco
from functools import wraps
import os, sys, time, string, json
os.chdir(os.path.abspath(os.path.join("dados_bancarios")))

# Programa principal

def user_choice(txt):
	choice = input(f"{txt}").strip()
	if choice == "":
		choice = "0"
	while choice.isdigit()==False:
		choice = input(f"{txt}").strip()
	return int(choice)




while True:
	Sistema = subclass_banco.Sub()
	system_ask_user = user_choice("\n >>> ")
	if system_ask_user == 4:
		decorativos.titulo("Volte sempre!")
		break
	
	if system_ask_user == 1:
		decorativos.load()
		Sistema.depositar()
	if system_ask_user == 2:
		decorativos.load()
		Sistema.sacar()
	if system_ask_user == 3:
		decorativos.load()
		os.system("clear")
		decorativos.titulo("Selecione uma opção")
		subclass_banco.verificar()
	if system_ask_user > 4 or system_ask_user <= 0:
		print(" Essa opção não existe!")
		time.sleep(2)
		os.system("clear")
	
	
	
