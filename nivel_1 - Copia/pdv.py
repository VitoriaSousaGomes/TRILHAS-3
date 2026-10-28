valorCompra = float(input("Qual o valor da compra? "))
compras = []
while valorCompra < 0:
    print("Valor invalido! Digite um valor POSITIVO.")
    valorCompra = float(input("Qual o valor da compra? "))

valoresOriginais = []
descontos = []
while valorCompra != 0:
    idade = int(input("Qual a idade do cliente? "))
    while idade < 0:
        print("Idade invalido! Digite um valor POSITIVO.")
        idade = int(input("Qual a idade do cliente? "))

    desconto_cupom = 0.0 
    descontoQuantidade = 0.0
    descontoExtra = 0.0
    descontoIdade = 0.0

    quantidadeItens = int(input("Quantos itens foram comprados? "))
    while quantidadeItens < 0:
        print("Valor invalido! Digite um valor POSITIVO.")
        quantidadeItens = int(input("Quantos itens foram comprados?"))

    valorIdade = valorCompra
    if idade >= 65: 
        descontoIdade = valorCompra * 0.20
        valorIdade = valorCompra - descontoIdade
    else:
        valorFinal = valorCompra
    if valorIdade > 100:
        descontoExtra = valorIdade * 0.10
        valorFinal = valorIdade - descontoExtra
    else:
        valorFinal = valorIdade

    if quantidadeItens > 3:
        descontoQuantidade = valorFinal * 0.05
        valorFinal = valorFinal - descontoQuantidade

    cupom = input("Digite o CUPOM de fidelidade: ")
    if cupom == "FIDELIDADE10": 
            desconto_cupom = valorFinal * 0.10
            valorFinal = valorFinal - desconto_cupom

    compras.append(valorFinal)
    descontos.append(descontoIdade + descontoExtra + descontoQuantidade + desconto_cupom)
    valoresOriginais.append(valorCompra)
    print(f"Entao valor para pagar: R${valorFinal:.2f}")

    valorCompra = float(input("Qual o valor da próxima compra? "))
    while valorCompra < 0:
        print("Valor invalido! Digite um valor POSITIVO.")
        valorCompra = float(input("Qual o valor da compra? "))

quantidade_compras = len(compras)
total_final = sum(compras)
total_bruto = sum(valoresOriginais)
total_descontos = sum(descontos)

print(f"Quantidade de Compras: {quantidade_compras}")
print(f"Total final: R$ {total_final:.2f}")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Total Descontos: R$ {total_descontos:.2f}")

with open("resumo.txt", "w") as arquivo:
    arquivo.write(f"Quantidade de compras: {quantidade_compras}\n")
    arquivo.write(f"Total final: R${total_final:.2f}\n")
    arquivo.write(f"Total bruto: R${total_bruto:.2f}\n")
    arquivo.write(f"Total dos descontos: R${total_descontos:.2f}\n")

    for indice in range(len(compras)):
        arquivo.write(f"Valor Original: R${valoresOriginais[indice]:.2f}\n")
        arquivo.write(f"Descontos aplicados: R${descontos[indice]:.2f}\n")
        arquivo.write(f"Valor final da compra: R${compras[indice]:.2f}\n")