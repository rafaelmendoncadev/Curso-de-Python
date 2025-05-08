
vendas_coca = 150
vendas_pepsi = 130
prunit_coca = 1.50
prunit_pepsi = 1.50
custo_loja = 2500

# 1. Qual foi o faturamento de Pepsi da Loja?

faturamento_pepsi = vendas_pepsi * prunit_pepsi
print("Faturamento de Pepsi: R$ " + str(faturamento_pepsi))

# 2. Qual foi o faturamento de Coca da Loja?
faturamento_coca = vendas_coca * prunit_coca
print("Faturamento de Coca: R$ " + str(faturamento_coca))

# 3. Qual foi o Lucro da loja?
lucro_loja = faturamento_pepsi + faturamento_coca - custo_loja
print("Lucro da loja: R$ " + str(lucro_loja))

if lucro_loja > 0:
    print("A loja teve lucro.")
elif lucro_loja == 0:
    print("A loja não teve lucro nem prejuizo.")
else:
    print("A loja teve prejuizo.")

# 4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). 
margem_loja = lucro_loja / (faturamento_pepsi + faturamento_coca)
print("Margem da loja:", margem_loja)

#A maioria das empresas trabalham com um Código para cada produto que possuem. 
# A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para 
# cada produto.
#Ex: 
#Coca -> Código: BEB1300543<br>
#Pepsi -> Código: BEB1300545<br>
#Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
#Vodka Smirnoff -> Código: BAC17675002<br>

#Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e 
# todas as bebidas alcóolicas tem o início do código "BAC".

#Crie um programa de consulta de bebida que, dado um código qualquer, 
# identifique se a bebida é alcóolica. O programa deve responder True para 
# bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, 
# use um input.

#Dica: Lembre-se do comando in para strings e sempre insira os códigos 
# com letra maiúscula para facilitar.
codigo_coca = "BEB1300543"
codigo_pepsi = "BEB1300545"
codigo_vinho = "BAC1546001"
codigo_vodka = "BAC17675002"

codigo_bebida = input("Digite o código da bebida: ")
if "BAC" in codigo_bebida:
    print("A bebida é alcóolica.")  
else:
    print("A bebida não é alcóolica.")  
    


