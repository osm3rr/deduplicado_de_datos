# librerias necesarias
import os
import hashlib
from collections import defaultdict

SOURCE_DIRECTORY = "documents"

def calculate_file_hash(filepath, block_size=65536):
    """Calcula el hash SHA-256 de un archivo de forma eficiente."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()

def find_duplicates():
    """Encuentra archivos duplicados en un directorio basándose en su hash."""
    hashes = defaultdict(list)
    print(f"Buscando duplicados en '{SOURCE_DIRECTORY}'...")

    for dirpath, _, filenames in os.walk(SOURCE_DIRECTORY):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                filepath = os.path.join(dirpath, filename)
                file_hash = calculate_file_hash(filepath)
                hashes[file_hash].append(filepath)

    # Filtrar solo los hashes que tienen más de un archivo asociado
    duplicates = {hash_val: files for hash_val, files in hashes.items() if len(files) > 1}
    
    if not duplicates:
        print("¡Buenas noticias! No se encontraron duplicados exactos.")
        return

    print(f"\nSe encontraron {len(duplicates)} grupos de archivos duplicados:")
    for i, (hash_val, files) in enumerate(duplicates.items(), 1):
        print(f"\n--- Grupo {i} (Hash: {hash_val[:10]}...) ---")
        for f in files:
            print(f"  - {f}")

if __name__ == "__main__":
    find_duplicates()