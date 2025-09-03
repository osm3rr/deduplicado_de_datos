# Detección de Archivos Duplicados en PDF

Este proyecto contiene dos utilidades en Python para identificar archivos PDF duplicados dentro de un directorio (`documents/`). Permite detectar duplicados exactos (por hash de archivo) y duplicados por contenido textual (ignorando metadatos y diferencias de formato).

---

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Estrategias de Deduplicado](#estrategias-de-deduplicado)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
  - [Detección de duplicados exactos](#detección-de-duplicados-exactos)
  - [Detección de duplicados por contenido textual](#detección-de-duplicados-por-contenido-textual)
- [Personalización](#personalización)
- [Notas sobre el directorio `documents/`](#notas-sobre-el-directorio-documents)
- [Licencia](#licencia)

---

## Descripción General

Este repositorio permite identificar archivos PDF duplicados en un directorio, utilizando dos estrategias complementarias:

1. **Deduplicado exacto por hash de archivo:** Detecta archivos idénticos bit a bit.
2. **Deduplicado por hash de contenido textual:** Detecta archivos con el mismo texto, aunque tengan diferencias en metadatos o estructura interna.

Ambas estrategias ayudan a mantener tus colecciones de documentos limpias y libres de duplicados, facilitando la gestión y el almacenamiento eficiente.

---

## Estrategias de Deduplicado

### 1. Deduplicado Exacto (Hash de Archivo)

- **¿Cómo funciona?**  
  El script recorre todos los archivos PDF en el directorio y calcula el hash SHA-256 de cada archivo completo. Si dos archivos tienen el mismo hash, son idénticos en todos sus bits (incluyendo metadatos, imágenes, etc.).
- **¿Cuándo usarlo?**  
  Cuando necesitas identificar duplicados exactos, sin importar el contenido.

### 2. Deduplicado por Contenido Textual

- **¿Cómo funciona?**  
  El script extrae el texto de cada PDF y calcula el hash SHA-256 solo del texto. Así, detecta duplicados aunque los archivos tengan diferencias en metadatos, fechas, estructura interna o imágenes, siempre que el texto sea el mismo.
- **¿Cuándo usarlo?**  
  Cuando te interesa identificar documentos con el mismo contenido, aunque hayan sido generados o guardados de forma diferente.

---

## Estructura del Proyecto

```
deduplicado_datos/
│
├── find_duplicate_hash_archivo.py   # Detección de duplicados exactos
├── find_duplicate_hash_texto.py     # Detección de duplicados por texto
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
└── documents/                       # Carpeta donde colocar los PDFs a analizar
    ├── archivo1.pdf
    ├── archivo2.pdf
    └── ...
```

---

## Requisitos

- Python 3.7 o superior
- Para deduplicado por texto: `langchain_community`, `pypdf`

---

## Instalación

1. Clona el repositorio o descarga los archivos.

```bash
git clone https://github.com/osm3rr/deduplicado_de_datos
```

2. Muevete a la carpeta del proyecto.

```bash
cd deduplicado_datos
```

3. Crea y activa un entorno virtual.

```bash
python -m venv .venv

# En macOS/Linux
source .venv/bin/activate  

# windows
.venv\Scripts\activate 
```

4. Instala las dependencias.

```bash
pip install -r requirements.txt
```

5. Coloca los archivos PDF a analizar en el directorio `documents/`.

---

## Uso

### Detección de duplicados exactos

```bash
python find_duplicate_hash_archivo.py
```
- Busca archivos PDF idénticos bit a bit en `documents/` y subcarpetas.

### Detección de duplicados por contenido textual

```bash
python find_duplicate_hash_texto.py
```
- Busca archivos PDF con el mismo texto, aunque tengan diferencias en metadatos o estructura.

---

## Personalización

- Cambia el directorio de búsqueda modificando la variable `SOURCE_DIRECTORY` en los scripts.
- Para buscar otros tipos de archivo, ajusta la extensión en la condición `if filename.lower().endswith('.pdf')`.

---

## Notas sobre el directorio `documents/`

- El directorio `documents/` está en `.gitignore` para evitar subir archivos privados o pesados.
- Puedes crear subdirectorios dentro de `documents/`; los scripts buscarán recursivamente.

---

## Licencia

Este proyecto está bajo la licencia MIT.

---
