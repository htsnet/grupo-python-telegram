# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 08:59:30 2022

@author: Hamilton Tenório da Silva
https://github.com/htsnet


DESAFIO DA SEMANA 05/03/2022

Caixa eletrônico 

O programa deve pergunta seu nome e número da conta depois disso ele deverá ter 3 opções sacar, depositar,sair 

Opção saca ele te enformar quanto dinheiro vc tem na conta se o valor for = 0 ele tem que informar vc precisa depositar algum valor primeiro 
Se o valor sacado for maior que o valor em contato ele tem que falar saldo para saque insuficiente 


Na opção depósito ele tem que mostrar o valor anterior e o novo valor
"""

nome = input("Qual é o seu nome? ")
conta = input("Qual é o número da sua conta? ")
saldo = 0
saldo_anterior = 0


while True:
    opcao = input("Qual a opção desejada? Sacar (S), Depositar (D) ou Sair (X)").upper()
    
    
    if opcao == "S":
        if saldo == 0:
            print("Você não tem saldo para efetuar um saque! Faça um depósito primeiro.")
        else:
            quanto = int(input("Qual o valor desejado? "))
            if quanto > saldo:
                print("Seu saldo não permite um saque neste valor.")
            else:
                print("Saque autorizado. Aproveite bem o dinheiro.")
                saldo -= quanto
    elif opcao == "D":
        quanto = int(input("Qual o valor que vai ser depositado? "))
        saldo += quanto
        print("Seu saldo anterior era R$", saldo_anterior)
    elif opcao == "X":
        break
    else:
        print("Esta opção não é válida. Escolha outra.")
    
    if saldo != saldo_anterior:    
        print(nome, ", seu saldo agora é de R$", saldo)
    
    saldo_anterior = saldo

