import os
import shutil

# Definición de rutas (Carpeta de descargas o donde estén los archivos)
ruta_origen = "./archivos_desordenados"

# Reglas de clasificación por extensión
reglas_clasificacion = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Datos": [".csv", ".xlsx", ".xls", ".json", ".sql"],
    "Codigo": [".py", ".cpp", ".h", ".java"]
}

def crear_carpetas_si_no_existen(ruta_base, carpetas):
    for nombre_carpeta in carpetas:
        ruta_completa = os.path.join(ruta_base, nombre_carpeta)
        if not os.path.exists(ruta_completa):
            os.makedirs(ruta_completa)

def organizar():
    # 1. Crear estructura de carpetas destino
    crear_carpetas_si_no_existen(ruta_origen, reglas_clasificacion.keys())
    # Carpeta para archivos no identificados
    crear_carpetas_si_no_existen(ruta_origen, ["Otros"])

    # 2. Recorrer cada archivo en la carpeta origen
    for archivo in os.listdir(ruta_origen):
        ruta_archivo = os.path.join(ruta_origen, archivo)

        # Saltar si es carpeta o archivo oculto
        if os.path.isdir(ruta_archivo) or archivo.startswith('.'):
            continue

        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()

        # 3. Determinar a qué carpeta pertenece
        destino_asignado = "Otros"
        for carpeta, lista_ext in reglas_clasificacion.items():
            if extension in lista_ext:
                destino_asignado = carpeta
                break

        # 4. Mover archivo
        ruta_destino = os.path.join(ruta_origen, destino_asignado, archivo)
        shutil.move(ruta_archivo, ruta_destino)
        print(f"✅ Movido: {archivo} ➔ {destino_asignado}")

if __name__ == "__main__":
    print("=== INICIANDO ORGANIZACIÓN AUTOMÁTICA ===")
    organizar()
    print("✅ Proceso finalizado. Todo está ordenado.")
