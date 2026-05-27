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
    
    # 1. Inicializamos el diccionario que guardará el árbol BFS
    arbol_bfs = {}
    
    print("\n--- Iniciando Evacuación (BFS) ---")

    while cola:
        nodo_actual, camino = cola.popleft()
        orden_visita.append(nodo_actual)
        print(f"Visitando: {nodo_actual}")

        # 2. Preparamos al nodo actual en el árbol para poder anotarle sus hijos
        if nodo_actual not in arbol_bfs:
            arbol_bfs[nodo_actual] = []

        # Caso Base: Llegamos al destino
        if nodo_actual == finish:
            pasos = len(camino) - 1
            # 3. Agregamos arbol_bfs a los valores de retorno
            return orden_visita, camino, pasos, True, arbol_bfs

        # Explorar vecinos
        aristas_vecinas = grafo_obj.adyacencias.get(nodo_actual, [])
        for arista in aristas_vecinas:
            vecino = arista.destino.nombre
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
                
                # 4. Registramos al vecino como hijo del nodo actual en nuestro árbol
                arbol_bfs[nodo_actual].append(vecino)

    # Si no encuentra ruta, también devuelve el árbol de lo que alcanzó a explorar
    return orden_visita, None, 0, False, arbol_bfs
