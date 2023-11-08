import time
import algoritmos as alg
import leituraEntrada as ent

# as linhas 7, 8, 9 e 10 são apenas para facilitar a vida já que ninguém quer ter que ficar escrevendo vetores aleatórios a cada execução para fazer a comparação

entrada = int (input ("digite o tamanho do vetor que será aplicado ao algoritmo (vetor maior que 1): "))

ent.entradaOrdenada(entrada)  # gera array ordenado - Melhor caso
ent.entradaAleatoria(entrada)  # gera array aleatória - Caso Médio
ent.entradaInvertida(entrada)  # gera array invertida - Pior caso

ordenado = ent.lerEntrada("vetor ordenado.txt")
aleatorio = ent.lerEntrada(
  "vetor aleatorio.txt")
invertido = ent.lerEntrada(
  "vetor invertido.txt")

Casos = ["Melhor Caso", "Caso Medio", "Pior Caso"]

Entradas = (ordenado, aleatorio, invertido)

Algoritmos = [
  alg.bubbleSort, 
  alg.insertionSort, 
  alg.selectionSort, 
  alg.heapSort,
  alg.quickSort, 
  alg.mergeSort, 
  alg.shellSort, 
  alg.combSort
]

Nomes = [
  'Bubble Sort', 
  'Insertion Sort', 
  'Selection Sort', 
  'Heap Sort', 
  'Quick Sort',
  'Merge Sort', 
  'Shell Sort', 
  'Comb Sort'
]

def rodarTodos () : 
  for algoritmo, algnome in zip(Algoritmos, Nomes):
    print(f"--- cálculo do tempo de execução do {algnome} ---- \n")
  
    for caso, entrada in zip(Casos, Entradas):
      start = time.perf_counter()
      algoritmo(entrada)
      end = time.perf_counter()
      print(f"{caso:<11} - Tempo: {end-start}s \n")
  
    print("\n ----------------------------------------------------- \n \n \n ")

def rodar1(nome,algoritmo):

  print(f"\n --- cálculo do tempo de execução do {nome} ---- \n Entrada = "+str(len(ordenado))+" posições \n") # entrada definida na linha 7 .  eu sei , mas queira uma forma mais perto de mudar a entrada, em vez de subir ate o começo da tela.
  for caso,entrada in zip(Casos, Entradas):  
    start = time.perf_counter()
    sort = algoritmo(entrada)
    end = time.perf_counter()
    print(f" {caso:<11} - Tempo: {end-start}s \n número de trocas : {sort[1]}")

opção = int (input ("\n 1 - utilizar 1 algoritmo \n 2 - rodar todos os algoritmos \n"))

if opção == 1 : 
  print ("\n 1 - Bubble Sort \n 2 - Selection Sort \n 3 - Insertion Sort \n 4 - Merge Sort \n 5 - Quick Sort \n 6 - Heap sort \n 7 - Shell Sort \n 8 - Comb Sort \n")

  algo = int (input("escolha um dos algoritmos pelo número da opção : "))

  if algo == 1 : 
    
    rodar1 ("Bubble sort" , alg.bubbleSort)

  elif algo == 2 : 

    rodar1 ("Selection sort" , alg.selectionSort)

  elif algo == 3 : 

    rodar1 ("Insertion sort" , alg.insertionSort)

  elif algo == 4 : 

    rodar1 ("Merge sort" , alg.mergeSort)

  elif algo == 5 : 

    rodar1 ("Quick sort" , alg.quickSort)

  elif algo == 6 : 

    rodar1 ("Heap sort" , alg.heapSort)

  elif algo == 7 : 

    rodar1 ("Shell sort" , alg.shellSort)

  elif algo == 8 : 

    rodar1 ("Comb sort" , alg.combSort)

  else : 

    print ("opcao invalida")

else : 

  rodarTodos ()