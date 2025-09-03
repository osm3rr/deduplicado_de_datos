# find_duplicate_hash_v2.py
import os
import hashlib
from collections import defaultdict
from langchain_community.document_loaders import PyPDFLoader

# --- CONFIGURACIÓN ---
# Directorio donde se encuentran los documentos a analizar.
SOURCE_DIRECTORY = "documents"

def extract_text_from_pdf(filepath):
    """
    Extrae todo el contenido de texto de un archivo PDF.
    Devuelve una cadena de texto vacía si ocurre un error.
    """
    # Esta función es crucial: nos permite ignorar metadatos, imágenes o
    # diferencias de formato, centrándonos únicamente en el contenido textual.
    try:
        loader = PyPDFLoader(filepath)
        pages = loader.load()
        # Se unen todas las páginas en una sola cadena de texto.
        full_text = "".join(page.page_content for page in pages)
        return full_text
    except Exception as e:
        # Informamos del error pero no detenemos el script, simplemente
        # omitimos este archivo en el análisis.
        print(f"Error procesando el archivo {filepath}: {e}")
        return ""

def find_content_duplicates():
    """
    Encuentra archivos duplicados basándose en el hash del contenido
    textual extraído de los PDFs.
    """
    # El defaultdict nos ayuda a agrupar las rutas de archivo por su hash de contenido.
    hashes = defaultdict(list)
    print(f"Buscando duplicados de contenido en '{SOURCE_DIRECTORY}'...")
    print("Este proceso puede tardar, ya que requiere leer cada PDF...")

    # Recorremos todos los archivos en el directorio de origen.
    for dirpath, _, filenames in os.walk(SOURCE_DIRECTORY):
        for filename in filenames:
            # Nos aseguramos de procesar únicamente archivos PDF.
            if filename.lower().endswith('.pdf'):
                filepath = os.path.join(dirpath, filename)
                
                # --- La lógica clave de esta versión ---
                # 1. Extraemos el texto en lugar de leer los bytes del archivo.
                content_text = extract_text_from_pdf(filepath)
                
                # 2. Solo si se extrajo texto, procedemos a calcular el hash.
                if content_text:
                    # Es necesario codificar el texto a bytes (usando utf-8) antes de hacer el hash.
                    content_hash = hashlib.sha256(content_text.encode('utf-8')).hexdigest()
                    # Agrupamos la ruta del archivo bajo el hash de su contenido.
                    hashes[content_hash].append(filepath)

    # --- Procesamiento y visualización de resultados (idéntico al script v1) ---

    # Filtramos para quedarnos solo con los hashes que aparecen más de una vez.
    duplicates = {hash_val: files for hash_val, files in hashes.items() if len(files) > 1}
    
    if not duplicates:
        print("\n¡Buenas noticias! No se encontraron duplicados basados en el contenido textual.")
        return

    print(f"\nSe encontraron {len(duplicates)} grupos de archivos con contenido textual idéntico:")
    for i, (hash_val, files) in enumerate(duplicates.items(), 1):
        print(f"\n--- Grupo {i} (Hash de contenido: {hash_val[:10]}...) ---")
        for f in files:
            print(f"  - {f}")

# --- Bloque de Ejecución Principal ---
if __name__ == "__main__":
    # Verificamos que las librerías necesarias estén instaladas.
    try:
        from langchain_community.document_loaders import PyPDFLoader
    except ImportError:
        print("Error: LangChain no está instalado.")
        print("Por favor, ejecuta: pip install langchain_community pypdf")
        exit(1)
        
    find_content_duplicates()