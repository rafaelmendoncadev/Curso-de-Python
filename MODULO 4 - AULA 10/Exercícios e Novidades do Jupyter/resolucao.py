
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




