# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:40:38 2022
"""

'''
Grupo Telegram Python
Desafio da Semana


Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e compraram alguns itens:

75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)

2 pacotes de macarrão: R$ 8,73 cada

1 pacote de Molho de tomate: R$ 3,45

420g Cebola: R$ 5,40/kg

250g de Alho: R$ 30/kg

450g de pães franceses: R$ 25/kg

Calcule quanto ficou para cada um.
'''

# nome dos amigos na república
team = ('Hamilton', 'Joca', 'Moacir', 'Demival', 'Jackson')

# lista de produtos adquiridos
# cada linha tem o nome, quantidade adquirida, preço unitário e unidade de medida
itens = [
    ('cerveja', 75, 2.2, 1),
    ('macarrao', 2, 8.73, 1),
    ('molho', 1, 3.45, 1),
    ('cebola', 420, 5.4, 1000),
    ('alho', 250, 30, 1000),
    ('pao', 450, 25, 1000)
    ]

total = 0
for i in itens:
    # divide o preço pela unidade de medida e multiplica pela quantidade
    subtotal = round(i[2] / i[3] * i[1], 2)
    total += subtotal

print("O valor para cada pessoa é R$", round(total / len(team), 2))
