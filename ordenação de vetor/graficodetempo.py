import matplotlib.pyplot as plt
import numpy as np

# Dados hipotéticos (tamanhos de vetor e tempos de execução)
tamanhos = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
bubble_sort_tempos = [0.1, 1.2, 15.3, 150.4, 1500.8, 15000.5, 150000.9]
insertion_sort_tempos = [0.2, 2.1, 30.2, 300.5, 3000.9, 30001.2, 300002.3]
selection_sort_tempos = [0.3, 3.5, 50.5, 500.7, 5003.0, 50010.3, 500010.5]

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando os gráficos para cada algoritmo
plt.plot(tamanhos, bubble_sort_tempos, label='Bubble Sort', marker='o', linestyle='-', color='b')
plt.plot(tamanhos, insertion_sort_tempos, label='Insertion Sort', marker='s', linestyle='-', color='g')
plt.plot(tamanhos, selection_sort_tempos, label='Selection Sort', marker='^', linestyle='-', color='r')

# Adicionando título e rótulos aos eixos
plt.title('Tempo de Execução dos Algoritmos de Ordenação', fontsize=14)
plt.xlabel('Tamanho do Vetor', fontsize=12)
plt.ylabel('Tempo de Execução (ms)', fontsize=12)

# Logaritmo no eixo X (para tamanhos maiores)
plt.xscale('log')
plt.yscale('log')

# Exibindo a legenda
plt.legend()

# Salvando o gráfico como imagem PNG
plt.savefig('grafico_ordem.png', dpi=300)