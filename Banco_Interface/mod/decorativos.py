# Estilo
from time import sleep
import time, os

def titulo(txt):
	print("-"*(len(txt)+4))
	print(" ", str(txt).upper())
	print("-"*(len(txt)+4))
	

def opc(*n):
	titulo("Bem-vindo ao simulador bancário!!")
	print(" É novo aqui? Cadastre-se em Conta!\n")
	for x, y in enumerate(n):
		print(f" [ {x+1} ] {y}")


def load():
	time.sleep(0.8)
	os.system("clear")
	print(" Carregando", end="")
	for x in range(3):
		sleep(1)
		print(".",end="", flush=True)
	sleep(1)
	os.system("clear")