from collections import deque

def ejecutar_bfs(grafo_obj, start: str, finish: str):
    if start not in grafo_obj.nodos or finish not in grafo_obj.nodos:
        return [], None, 0, False

    orden_visita = []
    cola = deque([(start, [start])])
    visitados = {start}

    while cola:
        nodo_actual, camino = cola.popleft()
        orden_visita.append(nodo_actual)

        if nodo_actual == finish:
            pasos = len(camino) - 1
            return orden_visita, camino, pasos, True

        aristas_vecinas = grafo_obj.adyacencias.get(nodo_actual, [])
        for arista in aristas_vecinas:
            vecino = arista.destino.nombre
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))

    return orden_visita, None, 0, False
