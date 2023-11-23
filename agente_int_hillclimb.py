import random

def calcular_tempo_total(caminho, matriz_distancias, cidades):
    """
    Calcula o tempo total de viagem ao longo de um caminho dado a matriz de distâncias.
    """
    tempo_total = 0
    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        indice_atual = cidades.index(cidade_atual)
        indice_proxima = cidades.index(proxima_cidade)
        tempo_total += matriz_distancias[indice_atual][indice_proxima]
    indice_ultimo = cidades.index(caminho[-1])
    tempo_total += matriz_distancias[indice_ultimo][cidades.index(caminho[0])]  # Retornar à cidade de origem
    return tempo_total

def gerar_caminho_aleatorio(cidades):
    """
    Gera um caminho aleatório entre as cidades.
    """
    caminho = list(cidades)
    random.shuffle(caminho)
    return caminho

def hill_climbing_manutencao(matriz_distancias, cidades, num_iteracoes):
    """
    Aplica o algoritmo de Hill Climbing para otimizar a rota dos técnicos de manutenção.
    """
    melhor_caminho = gerar_caminho_aleatorio(cidades)
    melhor_tempo_total = calcular_tempo_total(melhor_caminho, matriz_distancias, cidades)

    for _ in range(num_iteracoes):
        vizinho = list(melhor_caminho)
        i, j = sorted(random.sample(range(len(cidades)), 2))
        vizinho[i:j+1] = reversed(vizinho[i:j+1])
        novo_tempo_total = calcular_tempo_total(vizinho, matriz_distancias, cidades)

        if novo_tempo_total < melhor_tempo_total:
            melhor_caminho = vizinho
            melhor_tempo_total = novo_tempo_total

    return melhor_caminho, melhor_tempo_total

if __name__ == "__main__":
    # Matriz de Distâncias (tempo de viagem entre locais, em minutos)
    matriz_distancias = [
        [0, 5, 10, 15],
        [5, 0, 8, 7],
        [10, 8, 0, 12],
        [15, 7, 12, 0]
    ]

    # Lista de Cidades
    cidades = ['A', 'B', 'C', 'D']

    # Parâmetros do Hill Climbing
    num_iteracoes = 1000

    # Execução do Hill Climbing para Técnicos de Manutenção
    melhor_caminho, melhor_tempo_total = hill_climbing_manutencao(matriz_distancias, cidades, num_iteracoes)

    # Resultado
    print("Melhor Caminho para Técnicos de Manutenção:", melhor_caminho)
    print("Melhor Tempo Total de Viagem:", melhor_tempo_total, "minutos")

