import numpy as num

def entradaOrdenada (entrada) : 
  ordenado = num.arange (entrada) # array ordenado - Melhor caso
  arrayOrdenada = open ("vetor ordenado.txt" , "w")
  
  for posicao in range (entrada) : 
    if posicao != entrada - 1 : 
      arrayOrdenada.write (str (ordenado [posicao]) + ",")
    else : 
      arrayOrdenada.write (str (ordenado [posicao]))

def entradaAleatoria (entrada) : 
  aleatorio = num.random.randint (0, entrada, entrada) # array aleatória - Caso Médio
  arrayAleatoria = open ("vetor aleatorio.txt" , "w")
  
  for posicao in range (entrada) : 
    if posicao != entrada - 1 : 
      arrayAleatoria.write (str (aleatorio [posicao]) + ",")
    else : 
      arrayAleatoria.write (str (aleatorio [posicao]))

def entradaInvertida (entrada) :
  ordenado = num.arange (entrada)
  invertido = num.flip (ordenado) # array invertida - Pior caso
  arrayInvertida = open ("vetor invertido.txt" , "w")
  
  for posicao in range (entrada) : 
    if posicao != entrada - 1 : 
      arrayInvertida.write (str (invertido [posicao]) + ",")
    else : 
      arrayInvertida.write (str (invertido [posicao]))

def lerEntrada (arquivo) : 
  array = num.loadtxt (arquivo , dtype = "int", delimiter = ",")
  return array