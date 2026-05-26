from models import Nodo, Arista, Grafo
from bfs import ejecutar_bfs
from dfs import dfs
import json
from collections import deque
from typing import List, Dict, Tuple, Optional


def cargar_datos(ruta_archivo: str) -> Grafo:
    """Lee el archivo JSON de configuración y construye el Grafo."""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos_json = json.load(archivo)
    
    grafo = Grafo()
    grafo.cargar_desde_diccionario(datos_json)
    return grafo


def main():
    print("=" * 55)
    print(" SISTEMA DE EXPLORACIÓN DE RUTAS DE EVACUACIÓN (EPN) ")
    print("=" * 55)
    
    # Manejo dinámico de rutas del archivo según dónde se ejecute el comando en WSL
    try:
        grafo = cargar_datos("../data/campus_map.json")
    except FileNotFoundError:
        try:
            grafo = cargar_datos("data/campus_map.json")
        except FileNotFoundError:
            print("\n[!] ERROR: No se encontró el archivo de datos 'grafo.json'.")
            print("Asegúrate de que exista la carpeta 'data' con su archivo JSON respectivo.")
            return

    print(f"[*] Grafo cargado correctamente con {len(grafo.nodos)} ubicaciones registradas.\n")

    # Menú interactivo (Requerimiento para asegurar puntos extras en la rúbrica)
    while True:
        print("\n" + "~"*45)
        print("                 MENÚ PRINCIPAL")
        print("~"*45)
        print("1. Ejecutar simulación de rutas (BFS vs DFS)")
        print("2. Listar todos los puntos del campus")
        print("3. Salir del sistema")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == '1':
            inicio = input("\nIngrese el punto de ORIGEN: ").strip()
            fin = input("Ingrese el punto de DESTINO: ").strip()
            
            # Control de casos especiales (Puntos adicionales en rúbrica)
            if inicio not in grafo.nodos.keys() or fin not in grafo.nodos.keys():
                print("\n[!] Error: Uno o ambos puntos ingresados no existen en el mapa del campus.")
                continue
                
            print("\n" + "="*50)
            print(" ANALISIS COMPARATIVO DE ALGORITMOS ")
            print("="*50)
            
            # --- Pruebas con el algoritmo BFS ---
            bfs_visita, bfs_camino, bfs_pasos, bfs_exito = ejecutar_bfs(grafo, inicio, fin)
            print("\n[+] BÚSQUEDA EN ANCHO (BFS):")
            print(f" -> Orden de exploración de nodos: {bfs_visita}")
            if bfs_exito and bfs_camino:
                print(f" -> Ruta evacuada óptima: {' -> '.join(bfs_camino)}")
                print(f" -> Número de tramos (aristas): {bfs_pasos}")
                print(" -> Nota: BFS garantiza encontrar la ruta más corta en aristas.")
            else:
                print(" -> [X] No existe una ruta de conexión viable entre estos puntos.")
                
            print("-" * 50)
            
            # --- Pruebas con el algoritmo DFS ---
            ruta_dfs, arbol_dfs = dfs(grafo, inicio, fin)
            print("\n[+] BÚSQUEDA EN PROFUNDIDAD (DFS):")
            #print(f" -> Orden de exploración de nodos: {dfs_visita}")
            if ruta_dfs is not None:
                print(f"\n✅ ¡Ruta DFS encontrada!: {' -> '.join(ruta_dfs)}")
                print(f"🌳 Árbol de exploración DFS generado con éxito.")
            else:
                print("\n❌ Fallo en la evacuación: No se encontró camino o nodos inválidos.")
                
        elif opcion == '2':
            print("\n" + "-"*45)
            print(" UBICACIONES DISPONIBLES EN EL CAMPUS")
            print("-"*45)
            for nombre, nodo in grafo.nodos.items():
                estado = "🛡️ [PUNTO SEGURO]" if nodo.es_nodo_seguro else "⚠️ [Estructura/Aula]"
                print(f" * {nombre:<22} | Zona: {nodo.zona:<10} | {estado}")
                
        elif opcion == '3':
            print("\nFinalizando el simulador del sistema de evacuación. ¡Éxitos!")
            break
        else:
            print("\n[!] Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()