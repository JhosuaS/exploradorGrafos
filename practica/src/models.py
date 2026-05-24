from typing import List, Dict

class Nodo:
    """
    Representa una ubicación física en el campus.
    """
    def __init__(self, nombre: str, tipo: str, zona: str):
        self.nombre = nombre
        self.tipo = tipo
        self.zona =  zona
        self.es_nodo_seguro = (self.tipo.lower() == 'punto de encuentro')

    def __repr__(self):
        return f"Nodo({self.nombre})"

class Arista:
    """
    Representa la conexión (ruta de evacuación) entre dos nodos.
    """
    def __init__(self, origen: Nodo, destino: Nodo):
        self.origen = origen
        self.destino = destino

    def __repr__(self):
        return f"{self.origen.nombre} -> {self.destino.nombre}"

class Grafo:
    """
    Estructura principal del Grafo orientada a objetos.
    """
    def __init__(self):
        self.nodos: Dict[str, Nodo] = {}
        self.adyacencias: Dict[str, List[Arista]] = {}

    def cargar_desde_diccionario(self, datos_json: dict):
        """
        Lee el formato `nodo: [lista_vecinos]` y construye los objetos.
        """
        for nombre_nodo, datos in datos_json.items():
            tipo_nodo = datos["tipo"]
            zona_nodo = datos["zona"]
            nuevo_nodo = Nodo(nombre_nodo, tipo_nodo, zona_nodo)
            self.nodos[nombre_nodo] = nuevo_nodo
            self.adyacencias[nombre_nodo] = []

        for nombre_origen, datos in datos_json.items():
            lista_vecinos = datos["vecinos"]

            for nombre_destino in lista_vecinos:
                nodo_origen_obj = self.nodos[nombre_origen]
                nodo_destino_obj = self.nodos[nombre_destino]
                nueva_arista = Arista(nodo_origen_obj, nodo_destino_obj)
                self.adyacencias[nombre_origen].append(nueva_arista)