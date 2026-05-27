from collections import deque

def ejecutar_bfs(grafo_obj, start: str, finish: str):
    """
    Algoritmo BFS 
    """
    if start not in grafo_obj.nodos or finish not in grafo_obj.nodos:
        print(f"Error: el nodo {start} y/o el nodo {finish} no existen en el grafo")
        return [], None, 0, False, {}

    orden_visita = []
    cola = deque([(start, [start])])
    visitados = {start}
    

    arbol_bfs = {}
    
    print("\n--- Iniciando Evacuación (BFS) ---")

    while cola:
        nodo_actual, camino = cola.popleft()
        orden_visita.append(nodo_actual)
        print(f"Visitando: {nodo_actual}")

    
        if nodo_actual not in arbol_bfs:
            arbol_bfs[nodo_actual] = []

        # Caso Base: Llegamos al destino
        if nodo_actual == finish:
            pasos = len(camino) - 1
  
            return orden_visita, camino, pasos, True, arbol_bfs

        # Explorar vecinos
        aristas_vecinas = grafo_obj.adyacencias.get(nodo_actual, [])
        for arista in aristas_vecinas:
            vecino = arista.destino.nombre
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
                
 
                arbol_bfs[nodo_actual].append(vecino)

    return orden_visita, None, 0, False, arbol_bfs
