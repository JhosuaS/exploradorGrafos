def dfs(grafo_obj, nodo_actual: str, nodo_fin: str, visitados=None, camino=None, arbol_dfs=None):
    """
    Algoritmo DFS recursivo integrado con POO.
    Devuelve una tupla: (camino_encontrado, arbol_dfs)
    """
    if (nodo_actual not in grafo_obj.nodos) or (nodo_fin not in grafo_obj.nodos) :
        print(f"Error el nodo {nodo_actual} y/o el nodo {nodo_fin} no existen en el grafo")
        return None, None

    if visitados is None:
        visitados = []
        camino = []
        arbol_dfs = {}
        print("\n--- Iniciando Evacuación (DFS Recursivo) ---")

    visitados.append(nodo_actual)
    camino.append(nodo_actual)
    print(f"Visitando: {nodo_actual}") 

    # 3. Caso Base: ¡Encontramos el punto de encuentro!
    if nodo_actual == nodo_fin:
        return camino, arbol_dfs

    arbol_dfs[nodo_actual] = [] 

    for arista in grafo_obj.adyacencias[nodo_actual]:
        vecino = arista.destino.nombre

        if vecino not in visitados:
            arbol_dfs[nodo_actual].append(vecino)

            resultado_camino, resultado_arbol = dfs(grafo_obj, vecino, nodo_fin, visitados, camino, arbol_dfs)
            if resultado_camino is not None:
                return resultado_camino, resultado_arbol

    camino.pop()
    
    return None, arbol_dfs