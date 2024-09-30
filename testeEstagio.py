
# PERGUNTA 1
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)


# PERGUNTA 2 

def eh_fibonacci(numero):
    def eh_quadrado_perfeito(x):
        raiz = int(x**0.5)
        return raiz * raiz == x

    return eh_quadrado_perfeito(5 * numero**2 + 4) or eh_quadrado_perfeito(5 * numero**2 - 4)


numero_informado = int(input("Informe um número: "))

if eh_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci.")


# PERGUNTA 3 

faturamento_diario = {
    "faturamento_diario": [
        {"dia": 1, "valor": 2200.00},
        {"dia": 2, "valor": 3500.00},
        {"dia": 3, "valor": 1800.00},
        {"dia": 4, "valor": 4000.00},
        {"dia": 5, "valor": 0.00},
        {"dia": 6, "valor": 0.00},
        {"dia": 7, "valor": 3700.00},
        {"dia": 8, "valor": 2900.00},
        {"dia": 9, "valor": 3200.00},
        {"dia": 10, "valor": 2500.00},
        {"dia": 11, "valor": 2800.00},
        {"dia": 12, "valor": 0.00},
        {"dia": 13, "valor": 3000.00},
        {"dia": 14, "valor": 4100.00},
        {"dia": 15, "valor": 4500.00},
        {"dia": 16, "valor": 2700.00},
        {"dia": 17, "valor": 3400.00},
        {"dia": 18, "valor": 0.00},
        {"dia": 19, "valor": 3600.00},
        {"dia": 20, "valor": 4000.00},
        {"dia": 21, "valor": 0.00},
        {"dia": 22, "valor": 3800.00},
        {"dia": 23, "valor": 5000.00},
        {"dia": 24, "valor": 0.00},
        {"dia": 25, "valor": 4700.00},
        {"dia": 26, "valor": 4300.00},
        {"dia": 27, "valor": 0.00},
        {"dia": 28, "valor": 3700.00},
        {"dia": 29, "valor": 3900.00},
        {"dia": 30, "valor": 4100.00}
    ]
}

def calcular_faturamento(dados):
    faturamento_util = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]

    if len(faturamento_util) == 0:
        print("Não há dados de faturamento para processar.")
        return

    menor_faturamento = min(faturamento_util)
    maior_faturamento = max(faturamento_util)

    media_mensal = sum(faturamento_util) / len(faturamento_util)

    dias_acima_da_media = sum(1 for f in faturamento_util if f > media_mensal)

    print(f"Menor valor de faturamento em um dia útil: R$ {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento em um dia útil: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

calcular_faturamento(faturamento_diario)

# PERGUNTA 4 

faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcular_percentuais(dados):
    total_faturamento = sum(dados.values())

    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in dados.items()}

    print(f"Faturamento total: R$ {total_faturamento:.2f}\n")
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

calcular_percentuais(faturamento_por_estado)


# PERGUNTA 5 

def inverter_string(s):
    return s[::-1]

string_original = "desenvolvedor"

string_invertida = inverter_string(string_original)

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")

