# PDV com Descontos — Python

## Objetivo

Desenvolver um sistema simples de Ponto de Venda (PDV) em Python que calcule descontos nas compras de acordo com a idade do cliente e o valor da compra, além de apresentar um resumo das vendas realizadas.

## Como funciona

O programa solicita o valor da compra e a idade do cliente. Em seguida, verifica se existem descontos a serem aplicados.

As regras de desconto são:

- Clientes com idade igual ou superior a 65 anos recebem 20% de desconto.
- Se o valor da compra, após o desconto por idade, for maior que R$ 100,00, é aplicado mais 10% de desconto sobre esse valor já descontado.
- O valor final é exibido em reais, com duas casas decimais.
- O programa continua recebendo compras até que o usuário digite `0` como valor da compra.
- Valores negativos de compra e idade são rejeitados, e o programa solicita um novo valor.

Ao final, o sistema apresenta a quantidade de compras, o total bruto, o total de descontos concedidos e o total final das compras.

## Como executar

1. Abra a pasta `[=nivel_1` no Visual Studio Code ou em um terminal.
2. Execute o seguinte comando:
python pdv.py

3. Digite o valor da compra e a idade do cliente quando solicitados.
4. Para encerrar o programa, digite `0` no valor da próxima compra.

## Tecnologias utilizadas

- Python 3
- Listas
- Estruturas condicionais (`if` e `else`)
- Estruturas de repetição (`while`)
- Funções nativas `len()` e `sum()`
- Método `.append()`
- Formatação de valores com f-strings

## Casos de teste

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

## Estrutura do projeto

nivel_1/
├── pdv.py
├── README.md
└── resumo.txt

## Funcionalidades extras (bônus)

Além das funcionalidades obrigatórias, o programa possui três funcionalidades extras:

1. **Desconto por quantidade:** aplica um desconto adicional de 5% quando o cliente compra mais de 3 itens. O desconto é calculado sobre o valor restante após os descontos anteriores.

2. **Cupom de fidelidade:** aplica um desconto adicional de 10% quando o cliente informa o cupom `FIDELIDADE10`. O desconto é calculado sobre o valor restante após os demais descontos.

3. **Salvamento do histórico:** ao finalizar as compras, o programa gera o arquivo `resumo.txt`, contendo a quantidade de compras, os totais gerais e os valores originais, descontos e valores finais de cada compra.

## Casos de teste (BÔNUS)
| Teste | Valor | Idade | Itens | Cupom | Valor final |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | R$ 100,00 | 30 | 4 | — | R$ 95,00 |
| 2 | R$ 150,00 | 70 | 4 | — | R$ 102,60 |
| 3 | R$ 150,00 | 70 | 4 | FIDELIDADE10 | R$ 92,34 |
| 4 | R$ 150,00 | 70 | 2 | ABC123 | R$ 108,00 |

```