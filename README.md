# Detección de Archivos Duplicados en PDF

Este proyecto contiene dos utilidades en Python para identificar archivos PDF duplicados dentro de un directorio (`documents/`). Permite detectar duplicados exactos (por hash de archivo) y duplicados por contenido textual (ignorando metadatos y diferencias de formato).

---

## Tabla de Contenidos

- [Descripción General](#descripción-general)
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

- **find_duplicate_hash_archivo.py**  
  Busca archivos PDF duplicados comparando el hash SHA-256 de cada archivo. Detecta duplicados exactos (bit a bit).

- **find_duplicate_hash_texto.py**  
  Busca archivos PDF duplicados comparando el hash SHA-256 del texto extraído de cada archivo. Detecta duplicados aunque los archivos tengan diferencias en metadatos o estructura, siempre que el contenido textual sea idéntico.

---

## Estructura del Proyecto
