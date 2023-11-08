import time
import algoritmos as alg
import leituraEntrada as ent
import subprocess

# Gráficos de 100,1000 e 10000

Algoritmos = [
  alg.bubbleSort, alg.insertionSort, alg.selectionSort, alg.heapSort,
  alg.quickSort, alg.mergeSort, alg.shellSort, alg.combSort
]

Nomes = [
  'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Heap Sort', 'Quick Sort',
  'Merge Sort', 'Shell Sort', 'Comb Sort'
]


def rodarTodos():
  for algoritmo, algnome in zip(Algoritmos, Nomes):
    print(f"--- cálculo do tempo de execução do {algnome} ---- \n")

    tempo_execucao_melhor = []
    tempo_execucao_medio = []
    tempo_execucao_pior = []
    numero_elementos = []

    for i in range(0, 3):
      if (i == 0):
        num = 10**2
      if (i == 1):
        num = 10**3
      if (i == 2):
        num = 10**4

      print(f"-- Para entrada com {num} elementos -- \n")
      ent.entradaOrdenada(num)  # gera array ordenado - Melhor caso
      ent.entradaAleatoria(num)  # gera array aleatória - Caso Médio
      ent.entradaInvertida(num)  # gera array invertida - Pior caso

      ordenado = ent.lerEntrada("vetor ordenado.txt")
      aleatorio = ent.lerEntrada("vetor aleatorio.txt")
      invertido = ent.lerEntrada("vetor invertido.txt")

      Casos = ["Melhor Caso", "Caso Medio", "Pior Caso"]

      Entradas = (ordenado, aleatorio, invertido)
      numero_elementos.append(num)
      for caso, entrada in zip(Casos, Entradas):
        start = time.perf_counter()
        sort = algoritmo(entrada)
        end = time.perf_counter()
        if (caso == "Melhor Caso"):
          tempo_execucao_melhor.append(end - start)
        if (caso == "Caso Medio"):
          tempo_execucao_medio.append(end - start)
        if (caso == "Pior Caso"):
          tempo_execucao_pior.append(end - start)
        print(
          f"{caso:<11} - Tempo: {end - start}s \n número de trocas: {sort[1]}")

        # Criar gráfico
        gnuplot_script = f"""
                set terminal png
                set output 'tempo_vs_numero_elementos_{algnome.replace(" ", "")}_{caso}.png'
                set ylabel 'Número de Elementos'
                set xlabel 'Tempo de Execução (s)'
                set title 'Tempo de Execução vs. Número de Elementos - {algnome} - {caso}'
                plot '-' with linespoints title '{algnome}', '-' with linespoints title ''
                """
        if (caso == "Melhor Caso"):
          plot_data = "\n".join(
            f"{x} {y}"
            for x, y in zip(tempo_execucao_melhor, numero_elementos))
        if (caso == "Caso Medio"):
          plot_data = "\n".join(
            f"{x} {y}" for x, y in zip(tempo_execucao_medio, numero_elementos))
        if (caso == "Pior Caso"):
          plot_data = "\n".join(
            f"{x} {y}" for x, y in zip(tempo_execucao_pior, numero_elementos))

        plot_data += "\ne\n" + plot_data  # Para criar dois conjuntos de pontos no mesmo gráfico

        with subprocess.Popen(['gnuplot', '-p'], stdin=subprocess.PIPE) as gp:
          gp.communicate(
            bytes(gnuplot_script, 'utf-8') + bytes(plot_data, 'utf-8'))

    print("\n ----------------------------------------------------- \n \n \n ")


rodarTodos()
