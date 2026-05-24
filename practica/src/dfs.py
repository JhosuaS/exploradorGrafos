def dfs_tree(nodo, grafo, searched, componentR, arbolDfs):
    componentR.append(nodo)
    searched[nodo] = True
    
    for vecino in grafo[nodo]:
        if not searched[vecino]:
            arbolDfs[vecino] = nodo
            dfs_tree(vecino, grafo, searched, componentR, arbolDfs)
            print("Finaliza", vecino)
            print("Vuelve a", nodo)
            print()

    return arbolDfs