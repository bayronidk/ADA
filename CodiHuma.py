import os
import heapq
import collections

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def generar_frecuencias(texto):
    return collections.Counter(texto)

def construir_arbol(frecuencias):
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola_prioridad)
    while len(cola_prioridad) > 1:
        izquierda = heapq.heappop(cola_prioridad)
        derecha = heapq.heappop(cola_prioridad)
        nodo_padre = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        nodo_padre.izquierda = izquierda
        nodo_padre.derecha = derecha
        heapq.heappush(cola_prioridad, nodo_padre)
    return cola_prioridad[0]

def generar_codificacion(arbol_huffman, codigo='', codificacion={}):
    if arbol_huffman.caracter:
        codificacion[arbol_huffman.caracter] = codigo
    else:
        generar_codificacion(arbol_huffman.izquierda, codigo + '0', codificacion)
        generar_codificacion(arbol_huffman.derecha, codigo + '1', codificacion)
    return codificacion

def codificar_texto(texto, codificacion):
    return ''.join(codificacion[caracter] for caracter in texto)

def guardar_archivos(texto_original, texto_codificado):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_texto_original = os.path.join(directorio_actual, 'texto_original.txt')
    ruta_texto_codificado = os.path.join(directorio_actual, 'texto_codificado.txt')
    with open(ruta_texto_original, 'w') as archivo_original:
        archivo_original.write(texto_original)
    with open(ruta_texto_codificado, 'w') as archivo_codificado:
        archivo_codificado.write(texto_codificado)

def main():
    texto = input("Por favor, introduce el texto: ")
    
    frecuencias = generar_frecuencias(texto)
    arbol_huffman = construir_arbol(frecuencias)
    codificacion = generar_codificacion(arbol_huffman)
    texto_codificado = codificar_texto(texto, codificacion)
    guardar_archivos(texto, texto_codificado)
    
    print("Texto original guardado en 'texto_original.txt'")
    print("Texto codificado guardado en 'texto_codificado.txt'")

if __name__ == "__main__":
    main()

